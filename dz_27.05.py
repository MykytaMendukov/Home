import requests
from bs4 import BeautifulSoup

#!
response = requests.get("https://uk.wikipedia.org/") #на сайті example.com немає потрібних для перевірки елементів

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     h2 = soup.find_all('h2')
#     if h2:
#         for i in h2:
#             h2_ = i.text.strip()
#             print(h2_)
#     else:
#         print(f'Елемент "h2" не був знайдений')

#2

response = requests.get("https://uk.wikipedia.org/wiki/%D0%9F%D0%B5%D1%81_%D1%81%D0%B2%D1%96%D0%B9%D1%81%D1%8C%D0%BA%D0%B8%D0%B9")
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     table = soup.find_all('table')
#     if table:
#         for table_ in table:
#             tr = table_.find_all('tr')
#             for tr_ in tr:
#                 td = tr_.find_all('td')
#                 for td_ in td:
#                     print(td_.text.strip())
#                 print()
#         else:
#             print('Елемент "table" не був знайдений')

#3
response = requests.get('https://example.com/')

# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     ex = soup.find_all(class_='example-class')
#     if ex:
#         for n in ex:
#             print(n)
#     else:
#         print('Error')

#4
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    h1 = soup.find('h1')
    if h1:
        print(h1.text.strip())
    else:
        print('Error')
