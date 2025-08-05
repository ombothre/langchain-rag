from services.rag_setup.setup import vector_setup
from services.scraper.scrape import scrape
from ai.chat import chat
 
INITIAL = False     # Change this to False after first time use

if INITIAL:
    # Setup
    scrape()
    vector_setup()

print(chat("What is EaseMyAi?"))