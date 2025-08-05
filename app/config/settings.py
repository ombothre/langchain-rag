from dotenv import load_dotenv
import os

class Utils:
    def __init__(self):
        load_dotenv()

        self.OLLAMA_API=os.environ["OLLAMA_API"]
        self.INDEX_DIR=os.environ["INDEX_DIR"]
        
utils = Utils()