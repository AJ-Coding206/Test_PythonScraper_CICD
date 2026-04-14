# main.py
import requests
from bs4 import BeautifulSoup

def run_scraper():
    url = "https://example.com"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1').text
        print(f"成功抓取網頁標題: {title}")
    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    run_scraper()