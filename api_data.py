import requests
from config import FMP_API_KEY, STOCK_TICKER

BASE_URL = "https://financialmodelingprep.com/api/v3"

def get_income_statement(limit=4):
    url = f"{BASE_URL}/income-statement/{STOCK_TICKER}?limit={limit}&apikey={FMP_API_KEY}"
    return requests.get(url).json()

# Similar functions: get_balance_sheet(), get_cashflow(), get_dividends(), etc.
print(get_income_statement())
