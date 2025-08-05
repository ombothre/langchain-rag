FROM python:3.11-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock* ./

RUN uv pip compile pyproject.toml --no-emit-index-url --no-header -o requirements.txt && \
    uv pip install --system -r requirements.txt

COPY app/ .

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
