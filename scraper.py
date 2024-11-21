import requests
from bs4 import BeautifulSoup
from datetime import datetime

import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = "https://www.theverge.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    # Find all <a> tags with the specific class
    articles = soup.find_all("a", class_="group-hover:shadow-underline-franklin")
    print("Articles Found:", len(articles))  # Debugging: Log how many articles are found

    headlines = []
    for article in articles:
        title = article.get_text(strip=True)  # Extract the title text
        link = article["href"]  # Extract the link
        if title and link:
            # Convert relative URLs to absolute URLs
            full_link = f"https://www.theverge.com{link}" if link.startswith("/") else link
            headlines.append({"title": title, "link": full_link})

    print("Headlines Scraped:", headlines)  # Debugging: Log the scraped data
    return headlines



if __name__ == "__main__":
    headlines = scrape_headlines()
    if headlines:
        print("Scraped Headlines:")
        for headline in headlines:
            print(f"- {headline['title']} ({headline['link']})")
    else:
        print("No headlines were found. Check the website structure or update the scraper.")





