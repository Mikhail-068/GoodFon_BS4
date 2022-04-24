# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
import requests
from time import sleep

n = int(input('Сколько страниц пройти?  '))
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/96.0.4664.45 Safari/537.36',
           'accept': '*/*'}

def image_block(url):
    html = requests.get(url=url, headers=HEADERS).text
    soup = BS(html, 'html.parser')
    block = soup.find_all('div', class_="wallpapers__item__wall")
    return block

def image_link(img):
    result = img.find('img', class_="wallpapers__item__img")['src']
    return result

def image_save(img, count):
    image = requests.get(img).content
    with open(f'C:\\Users\\Asus\\Desktop\\BS4\\download_img\\gerl_{count}.jpg', 'wb') as f:
        f.write(image)



count = 1
for p in range(n):
    url = f'https://www.goodfon.ru/catalog/girls/index-{(count)}.html'
    block = image_block(url)

    for i in range(len(block)):
        image_save(image_link(block[i]), count)

        count += 1
        # sleep(0.1)






