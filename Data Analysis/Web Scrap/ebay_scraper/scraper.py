# TODO
# 1. mabke a request to the ebay.com and get a page
# 2. Collect data from each detail page
# 3. Collect all links to detail pages of each product
# 4. Write scraped data to csv file

import requests
from bs4 import BeautifulSoup
import lxml
import csv
import pandas as pd



def get_page(url):
    response = requests.get(url)

    if not response.ok:
        print('Server responded:', response.status_code)
    else:
        soup = BeautifulSoup(response.text, features='lxml')
    return soup


def get_detail_data(soup):
    # get the title from the soup
    try:
        title = soup.find('h1', id='itemTitle')

        # removes a span tag from the tree, then completely destroys it and its contents
        title.span.decompose()
        title = title.text.strip()
    except:
        title = ''

    # get the price of the item
    try:
        p = soup.find('span', id=['prcIsum_bidPrice', 'prcIsum', 'mm-saleDescPrc', 'mm-saleDscPrc']).text.strip()
        currency, price = p.split(' ')
        price = price.split('/')[0]
        # print(currency)
        # print(price)
    except:
        currency = ''
        price = ''

    # get the stock of the item
    try:
        total_sold = soup.find('span', class_='vi-qtyS-hot-red').find('a').text.strip().split(' ')[0].replace('\xa0', '')
    except:
        total_sold = ''

    data = {
        'title': title,
        'price': price,
        'currency': currency,
        'total_sold': total_sold
    }

    return data


def get_index_data(soup):
    try:
        links = soup.find_all('a', class_='s-item__link')
    except:
        links = []

    urls = [item.get('href') for item in links]

    return urls


def write_csv(data, url):
    with open('output.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        row = [data['title'], data['price'], data['currency'], data['total_sold'], url]
        writer.writerow(row)


def read_csv():
    df = pd.read_csv('output.csv', header=None, index_col=None)
    df.columns = ['title', 'price', 'currency', 'total sold', 'url']
    df.to_csv("output.csv", index=False)


def main():

    pages = range(1, 3)
    # grab the page number from 1 to 2
    for page in pages:
        url = 'https://www.ebay.com/sch/i.html?&_nkw=iphone&_png=' + str(page)
        products = get_index_data(get_page(url))

        for link in products:
            data = get_detail_data(get_page(link))
            write_csv(data, link)

    read_csv()


if __name__ == '__main__':
    main()
