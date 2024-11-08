import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract content from paragraph tags
        content = ''
        for paragraph in soup.find_all('p'):
            content += paragraph.get_text() + ' '

        return content

    except Exception as e:
        print(f"Error scraping website: {e}")
        return None
