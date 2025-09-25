
import requests
from bs4 import BeautifulSoup
from datetime import datetime

#Choose a public news website
URL = "https://www.bbc.com/news"   

#Add headers (pretend to be a browser)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/119.0 Safari/537.36"
}

try:
    #  Fetch page with error handling
    response = requests.get(URL, headers=headers, timeout=10)
    response.raise_for_status()
    print("✅ Page fetched successfully")

    #  Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract headlines (look for h1, h2, h3)
    headlines = []
    for tag in soup.find_all(["h1", "h2", "h3"]):
        text = tag.get_text(strip=True)
        if text:
            headlines.append(text)

    # Remove duplicates
    headlines = list(set(headlines))

    #  Keep only top 10 headlines
    headlines = headlines[:10]

    #  Save with timestamped filename
    filename = f"headlines_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for i, headline in enumerate(headlines, 1):
            file.write(f"{i}. {headline}\n")

    print(f"✅ {len(headlines)} headlines saved to {filename}")

except requests.exceptions.RequestException as e:
    print(f"❌ Error fetching page: {e}")
