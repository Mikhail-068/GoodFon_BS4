import requests
from bs4 import BeautifulSoup

URL = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&oq=&aqs=chrome.0.69i59i450l8.625526j0j15&sourceid=chrome&ie=UTF-8'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (HTML, like Gecko) \
            Chrome/96.0.4664.45 Safari/537.36',
           'accept': '*/*'}

html = requests.get(URL, headers=HEADERS).text

soup = BeautifulSoup(html, 'lxml')
r = soup.find('span', class_='wob_t q8U8x').text
print(r)