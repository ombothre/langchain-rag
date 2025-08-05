import requests
from bs4 import BeautifulSoup, element
from urllib.parse import urljoin, urlparse
import os
import time
import hashlib
import json

base_url = "https://easemyai.com"
visited = set()
content_hashes = set()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36"
}

def is_internal_link(link: str) -> bool:
    parsed = urlparse(link)
    return parsed.netloc == "" or parsed.netloc == urlparse(base_url).netloc

def is_allowed(url: str) -> bool:
    parsed = urlparse(url)
    return url.startswith(base_url) and parsed.scheme in {"http", "https"}

def sanitize_path(url: str, ext: str = ".txt") -> str:
    parsed = urlparse(url)
    path = parsed.path.strip("/") or "index"
    query = parsed.query.replace("=", "_").replace("&", "_")
    filename = path.replace("/", "_") + ("_" + query if query else "")
    return filename + ext

def is_duplicate(text: str) -> bool:
    h = hashlib.md5(text.encode()).hexdigest()
    if h in content_hashes:
        return True
    content_hashes.add(h)
    return False

def extract_visible_text(soup: BeautifulSoup) -> str:
    for tag in soup(["script", "style", "noscript", "svg", "meta", "link"]):
        tag.decompose()
    main = soup.find("main") or soup.find("article") or soup.find("div", class_="content") or soup.body
    if not main:
        return ""
    text = main.get_text(separator="\n", strip=True)
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return "\n".join(lines)

def download_pdf(pdf_url: str):
    os.makedirs("pdfs", exist_ok=True)
    filename = sanitize_path(pdf_url, ext=".pdf")
    filepath = os.path.join("pdfs", filename)

    if os.path.exists(filepath):
        print(f"Already downloaded PDF: {filename}")
        return

    try:
        print(f"PDF: {pdf_url}")
        resp = requests.get(pdf_url, headers=headers, timeout=10)
        if resp.ok and resp.headers.get("Content-Type", "").startswith("application/pdf"):
            with open(filepath, "wb") as f:
                f.write(resp.content)
        else:
            print(f"Skipped invalid PDF: {pdf_url}")
    except Exception as e:
        log_failure(pdf_url, str(e))

def log_failure(url, error):
    with open("failures.log", "a") as f:
        f.write(f"{url} - {error}\n")

def save_text_file(url, text):
    os.makedirs("visible_text", exist_ok=True)
    filename = sanitize_path(url)
    filepath = os.path.join("visible_text", filename)
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)

def save_as_jsonl(url, text):
    os.makedirs("jsonl_data", exist_ok=True)
    filepath = os.path.join("jsonl_data", "scraped.jsonl")
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(json.dumps({"url": url, "text": text}) + "\n")

def scrape(url: str = base_url):
    
    visited.add(url)

    print(f"Scraping: {url}")
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        content_type = resp.headers.get("Content-Type", "")

        if "application/pdf" in content_type:
            download_pdf(url)
            return

        if "text/html" not in content_type or resp.status_code != 200:
            return

        soup = BeautifulSoup(resp.text, "html.parser")
        visible_text = extract_visible_text(soup)

        if not visible_text or len(visible_text.split()) < 100:
            print(f"Skipping short or empty content: {url}")
            return
        if is_duplicate(visible_text):
            print(f"Duplicate content: {url}")
            return

        save_text_file(url, visible_text)
        save_as_jsonl(url, visible_text)

        # Crawl more links
        for a in soup.find_all("a", href=True):
            if isinstance(a, element.Tag):
                href = a.get("href")
                if not href:
                    continue
                full_url = urljoin(url, str(href).strip())
                if full_url.endswith(".pdf"):
                    download_pdf(full_url)
                elif is_internal_link(full_url) and is_allowed(full_url):
                    scrape(full_url)

        time.sleep(1)

    except Exception as e:
        log_failure(url, str(e))