import requests

WEBSITE_URL = "https://example.com"

def check_website():
    try:
        response = requests.get(WEBSITE_URL)
        if response.status_code == 200:
            print(f"{WEBSITE_URL} is online!")
        else:
            print(f"{WEBSITE_URL} is down! Status code: {response.status_code}")
    except requests.RequestException:
        print(f"Error: Unable to reach {WEBSITE_URL}")

check_website()