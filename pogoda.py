import requests
from bs4 import BeautifulSoup

URL = 'https://ria.ru/world/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) \
            Chrome/96.0.4664.45 Safari/537.36',
           'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url=url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='list-item__content')
    print(items.text)
    for i in items:
        print(i.text)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        # Если достучались до страницы -  получаем её контент!
        get_content(html.text)  # html текст страницы
    else:
        print('Видимо что-то случилось...')



parse()