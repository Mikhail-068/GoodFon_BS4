# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/96.0.4664.45 Safari/537.36',
           'accept': '*/*'}

header = ['Фильм', 'Рейтинг', 'Ссылка']

url = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&aqs=chrome.0.69i59j69i61j69i60j69i61.1036j0j15&sourceid=chrome&ie=UTF-8'
r = requests.get(url=url).text
soup = BeautifulSoup(r, 'lxml')
# block = soup.find_all('div', class_="post-title")
print(r)
# data = []
# for p in range(1, 31):
#     url = f'http://torrfan.org/page/{p}'
#     r = requests.get(url=url, headers=HEADERS, params=None).text
#     soup = BeautifulSoup(r, 'lxml')
#     # sleep(0.5)
#     block = soup.find_all('div', class_="post-title")
#     point = soup.find_all('a', class_='orating_res')
#     download = soup.find_all('li', class_='more')
#
#     for i in range(len(block)):
#         data.append([block[i].text, point[i].text, download[i].find('a').get('href')])
#
#     print(f'Страница: {p}')
#
# df = pd.DataFrame(data, columns=header)
# df.to_csv('Films.csv', sep=';', encoding='cp1251')