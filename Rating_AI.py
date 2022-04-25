# -*- coding: cp1251 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) \
            Chrome/96.0.4664.45 Safari/537.36',
           'accept': '*/*'}

header = ['Name', 'Point']

data = []


def Get(p):
    url = f'https://neuraluniversity.getcourse.ru/pl/user/scale/view-results?id=43934&userId=84746556&page={p}'
    r = requests.get(url=url, headers=HEADERS, params=None).text
    soup = BeautifulSoup(r, 'lxml')
    # sleep(0.5)
    name = soup.find_all('div', class_="user-icon")
    point = soup.find_all('td')
    return name, point


count = 1
ind_point = []
for i in range((50 * 3) * 7):
    ind_point.append(count)
    count += 3

data = []
for p in range(1, 8):
    name, point = Get(p)
    for i in range(len(name)):
        data.append([name[i].text, point[ind_point[i]].text])

    print(f'Страница: {p}')

df = pd.DataFrame(data, columns=header)
df.to_csv('Рейтинг_УИИ.csv', sep=';', encoding='cp1251')
