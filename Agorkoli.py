import requests
from bs4 import BeautifulSoup

def get_Agorkoli(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('h2')

    for index, headlines in enumerate(headlines, start=1):
        print(f"{index}. {headline.text.strip()}")
if __name__ == "__main__":
    news_url = " https://www.verywellmind.com"
    get_Agorkoli(news_url)

