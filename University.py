# -*- coding: cp1251 -*-
import requests
from bs4 import BeautifulSoup
from config import HEADERS
import pandas as pd

data = []
def page(n):
    url = f'https://neuraluniversity.getcourse.ru/pl/user/scale/view-results?id=43934&userId=84746556&page={n}'
    r = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(r, 'lxml')
    info = soup.find_all('td')

    for i in range(len(info)):
        if i % 3 == 0:
            name = info[i].text
            point = info[i + 1].text.split()[0]
            data.append([name, point])

for p in range(1,8):
    page(p)
    print(f'Страница: {p}')

header = ['Name', 'Point']
df = pd.DataFrame(data, columns=header)
df.to_csv('Рейтинг_УИИ_апрель_2022.csv', sep=';', encoding='cp1251')