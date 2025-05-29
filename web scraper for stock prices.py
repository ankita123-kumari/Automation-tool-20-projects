import requests
from bs4 import BeautifulSoup
import pandas as pd
import yfinance as yf

# Define the stock symbol
STOCK_SYMBOL = "AAPL"  # Change to your preferred stock

# Yahoo Finance Scraper URL
STOCK_URL = f"https://finance.yahoo.com/quote/{STOCK_SYMBOL}"

# Function to scrape stock price from Yahoo Finance website
def get_stock_price_scraper():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    
    response = requests.get(STOCK_URL, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Try different methods to find the stock price
        price_tag = soup.find("fin-streamer", {"data-test": "qsp-price"})  # Try this first
        if not price_tag:
            price_tag = soup.find("span", {"class": "Fw(b) Fz(36px) Mb(-4px) D(ib)"})  # Alternative

        return price_tag.text.strip() if price_tag else "Price not found"
    
    return "Failed to fetch data"

# Function to get stock price using Yahoo Finance API (yfinance)
def get_stock_price_api():
    try:
        stock = yf.Ticker(STOCK_SYMBOL)
        latest_price = stock.history(period="1d")["Close"].iloc[-1]
        return round(latest_price, 2)
    except Exception as e:
        return f"API Error: {str(e)}"

# Fetch data using both methods
scraped_price = get_stock_price_scraper()
api_price = get_stock_price_api()

# Save stock data to CSV
stock_data = pd.DataFrame({
    "Stock": [STOCK_SYMBOL],
    "Scraped Price": [scraped_price],
    "API Price": [api_price]
})

stock_data.to_csv("stock_prices.csv", index=False)

print("Stock Prices Scraped & Saved Successfully!")