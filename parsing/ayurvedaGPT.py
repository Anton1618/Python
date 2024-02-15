'''Парсинг https://shantiom.store/shop/ayurveda-dlya-zdorovya/ayurvedicheskie-preparaty/
'''

import requests
from bs4 import BeautifulSoup
import csv

def get_products(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    product_cards = soup.find_all('div', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')

    products = []

    for card in product_cards:
        product = {}
        title_elem = card.find('h2', class_='woocommerce-loop-product__title')
        if title_elem:
            product['title'] = title_elem.text
        price_elem = card.find('span', class_='woocommerce-Price-amount amount')
        if price_elem:
            product['price'] = price_elem.text
        product['link'] = card['href']
        product['sku'], product['manufacturer'], product['description'] = get_product_details(product['link'])
        products.append(product)

    return products

def get_product_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    sku_elem = soup.find('span', class_='sku')
    if sku_elem:
        sku = sku_elem.text
    else:
        sku = ''
    manufacturer_elem = soup.find('span', class_='posted_in')
    if manufacturer_elem:
        manufacturer = manufacturer_elem.text.split(':')[-1].strip()
    else:
        manufacturer = ''
    description_elem = soup.find('div', class_='woocommerceabs-panel woocommerce-Tabs-panel--description')
    if description_elem:
        description = description_elem.text.strip()
    else:
        description = ''

    return sku, manufacturer, description

def get_total_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pages_elem = soup.find('a', class_='page-numbers')
    if pages_elem:
        pages = int(pages_elem['href'].split('/')[-2])
    else:
        pages = 1

    return pages

def save_to_csv(products, filename='products.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Tilda UID', 'SKU', 'Category', 'Title', 'Description', 'Text', 'Price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for product in products:
            writer.writerow({
                'Tilda UID': '',
                'SKU': product['sku'],
                'Category': 'Ayurveda_health_preparation',
                'Title': product['title'],
                'Description': product['manufacturer'],
                'Text': product['description'],
                'Price': product['price']
            })

def main():
    base_url = 'https://shantiom.store/shop/ayurveda-dlya-zdorovya/ayurvedicheskie-preparaty/page/'
    all_products = []

    total_pages = get_total_pages(base_url + '1/')

    for page in range(1, total_pages + 1):
        url = base_url + str(page) + '/'
        products = get_products(url)
        all_products.extend(products)

    if all_products:
        save_to_csv(all_products)
    else:
        print('No products found.')

if __name__ == '__main__':
    main()