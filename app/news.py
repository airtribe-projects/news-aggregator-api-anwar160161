import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GNEWS_API_KEY")

def fetch_news(query):
    url = (
        f"https://gnews.io/api/v4/search"
        f"?q={query}"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return []

    return response.json().get("articles", [])