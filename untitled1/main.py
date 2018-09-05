import requests
import re
from bs4 import BeautifulSoup

sale_logic = 0


def get_html(url):
    r = requests.get(url)
    return r.text


def get_product_name(html):
    soup = BeautifulSoup(html, 'lxml')
    result = str(soup.find('h1', class_='product-name')).split('>')[1].split('<')[0]
    return result


def get_price_sale(html):
    global sale_logic
    soup = BeautifulSoup(html, 'lxml')
    result = str(soup.find('span', id='j-sku-discount-price')).split('>')[1].split('<')[0]
    if result != '':
        sale_logic = 0
        return result
    else:
        lowPrice = str(soup.find('span', itemprop='lowPrice')).split('>')[1].split('<')[0]
        highPrice = str(soup.find('span', itemprop='highPrice')).split('>')[1].split('<')[0]
        sale_logic = 1
        return (lowPrice + ' - ' + highPrice)


def get_price(html):
    soup = BeautifulSoup(html, 'lxml')
    result = str(soup.find('span', id='j-sku-price')).split('>')[1].split('<')[0]
    return result


def get_sale(html):
    soup = BeautifulSoup(html, 'lxml')
    result = str(soup.find('span', class_='p-discount-rate')).split('>')[1].split('<')[0]
    return result


def get_delivery(html):
    soup = BeautifulSoup(html, 'lxml')
    result = str(soup.find('span', class_='logistics-cost')).split('>')[1].split('<')[0]
    if result != '':
        return result
    else:
        return '0'

def get_time_sale(html):
    soup = BeautifulSoup(html, 'lxml')
    result = str(soup.find('span', class_='p-eventtime-left')).split('>')[1].split('<')[0]
    if result != '':
        return result
    else:
        return '0'

def get_photo(html):
    soup = BeautifulSoup(html, 'lxml')
    result = soup.find_all('span', class_='img-thumb-item')
    return result


def main():
    text = get_html('https://ru.aliexpress.com/item/Latest-Lightning-shaped-4-Layers-Smoking-Herb-Grinders-Weed-Tobacco-Cigarette-Quality-Grinder-Hookah-Fumar-Hierba/32801554606.html')
    name = get_product_name(text)
    print('Название: ' + name)

    price = get_price(text).replace(" ", "").replace(',', '.')
    print('Цена: ' + str(price) + ' руб')

    try:
        price_sale = get_price_sale(text).replace(' ', '').replace(',', '.')
        print('Цена со скидкой: ' + str(price_sale) + ' руб')

        if sale_logic == 0:
            sale = '-' + str((round(100 - (float(price_sale) * 100 / float(price)))))
        elif sale_logic == 1:
            sale = get_sale(text)
        print('Скидка: ' + str(sale) + '%')

        time_sale = get_time_sale(text)
        print(re.sub('^\s+', '', time_sale))

    except Exception:
        price_sale = 0

    delivery = get_delivery(text).replace(' ', '').replace(',', '.')
    print('Доставка: ' + str(delivery) + ' руб')

    for i in get_photo(text):
        print(i.find('img')['src'][:-10])


if __name__ == '__main__':
    main()
