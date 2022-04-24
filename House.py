# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
import requests
from time import sleep

# n = int(input('Сколько страниц пройти?  '))
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/96.0.4664.45 Safari/537.36',
           'accept': '*/*'}

def image_block(url):
    html = requests.get(url=url, headers=HEADERS).text
    soup = BS(html, 'html.parser')
    block = soup.find('div', class_="pb-PreviewList preview-list__tile")
    return block




def image_link(img):
    result = img.find('a', class_="b-PhotoPreview __size_responsive")['href']
    return result

def image_save(img, count):
    image = requests.get(img).content
    with open(f'C:\\Users\\Asus\\Desktop\\BS4\\download_img\\gerl_{count}.jpg', 'wb') as f:
        f.write(image)





url = 'https://www.inmyroom.ru/photos/spalnya/loft'
block = image_block(url)
# print(len(block))
block2 =  block.find_all('div')
count = 1
for i in range(len(block2)):
    if i%2!=0:
        if 'None' != str(block2[i].find('div', class_='b-PhotoPreview_pic')):
            image_save(block2[i].find('div', class_='b-PhotoPreview_pic')['data-src'], count)
            count+=1



