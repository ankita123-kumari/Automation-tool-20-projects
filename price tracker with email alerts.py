import requests
import smtplib
from email.mime.text import MIMEText

PRODUCT_URL = "https://example.com/product"
TARGET_PRICE = 100  # Set your desired price
EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"

def check_price():
    response = requests.get(PRODUCT_URL)
    price = float(response.json()["price"])  # Modify based on actual API response

    if price < TARGET_PRICE:
        send_email(price)

def send_email(price):
    msg = MIMEText(f"Price dropped to {price}! Buy now: {PRODUCT_URL}")
    msg["Subject"] = "Price Alert!"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, EMAIL, msg.as_string())

check_price()