import requests
from bs4 import BeautifulSoup

def extract_article_text(url):
    try:
        # 1️⃣ Fetch the page
        response = requests.get(url, timeout=10, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        })
        response.raise_for_status()

        # 2️⃣ Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 3️⃣ Find the main container s— many sites use these
        container = (
            soup.find('article') or
            soup.find('div', class_='article-content') or
            soup.find('div', class_='post-content') or
            soup.find('div', class_='entry-content') or
            soup.find('div', class_='main-content')
        )

        # 4️⃣ If we didn’t find any of those, just use the whole page
        if not container:
            container = soup

        # 5️⃣ Extract all <p> tags inside
        paragraphs = container.find_all('p')
        content = "\n\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))

        # 6️⃣ Clean and return
        return content if content else "⚠️ No readable content found."

    except Exception as e:
        return f"❌ Error: {e}"