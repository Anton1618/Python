import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://stopgame.ru/news')
html = BS(r.content, 'html.parser')

for el in html.select('._default-grid_4loqg_213'):
    title = el.select('div', class_='_content_1tbpr_142 > ._title_1tbpr_49')
    print(title[0].text)