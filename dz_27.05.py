import requests
from bs4 import BeautifulSoup

#!
response = requests.get("https://example.com")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    h2 = soup.find_all('h2')
    if h2:
        for i in h2:
            h2_ = i.text.strip()
            print(h2_)
    else:
        print(f'Елемент "h2" не був знайдений')

