from dotenv import load_dotenv
import os

load_dotenv()
FMP_API_KEY = os.getenv("FMP_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
STOCK_TICKER = 'MSFT'  # Use US stock code
