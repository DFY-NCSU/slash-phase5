"""
Copyright (c) 2021 Rohan Shah
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Slash
"""

# package imports
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from threading import Thread

# local imports
import src.formattr as form
# from src.configs_mt import AMAZON, WALMART, COSTCO, BESTBUY, scrape_ebay, scrape_target
from src.configs_mt import WALMART, BESTBUY, COSTCO, scrape_ebay, scrape_target
from src.scraper_ct import search_ct

class search(Thread):
    def __init__(self, query, config):
        self.result = {}
        self.query = query
        self.config = config
        super(search,self).__init__()
        
    def run(self):
        """Scrape the given config for a specific item

        Parameters
        ----------
        query: str
            Query of item we are looking for
        config: dict
            Configuration for site we are scraping

        Returns
        ----------
        products: list
            List of items returned from website
        """
        
        self.query = form.formatSearchQuery(self.query)
        URL = self.config['url'] + self.query

        # fetch url
        page = self.httpsGet(URL)
        if not page:
            self.result = []

        results = []
        # begin parsing page content
        if page:
            results = page.find_all(self.config['item_component'], self.config['item_indicator'])
        products = []
        print(len(results))
        for res in results:
            if self.config['site'] == 'bestbuy':
                # Extract the title
                title_tag = res.select_one('h4.sku-title a')
                title = title_tag.get_text(strip=True) if title_tag else ''

                # Extract the price
                price_tag = res.select_one('div.priceView-hero-price span')
                price = price_tag.get_text(strip=True) if price_tag else ''

                # Extract the product link
                link_tag = res.select_one('h4.sku-title a')
                link = link_tag['href'] if link_tag else ''

                # Extract the image link
                img_tag = res.select_one('a.image-link img')
                img_link = img_tag['src'] if img_tag else ''

                # Formulate the product information
                product = form.formatResultBestBuy(self.config['site'], title, price, link, img_link)

                # Append to products if required fields are populated
                if product['title'] and product['price'] and product['link']:
                    products.append(product)
            else:
                title = res.select(self.config['title_indicator'])
                # price = res.select(self.config['price_indicator'])
                price_div = res.find('div', {'data-automation-id': 'product-price'}).find('span', {'class': 'w_iUH7'})
                price_parts = [span.get_text(strip=True) for span in price_div if span.get_text(strip=True)][0]
                price = price_parts.split()[-1]
                link = res.select(self.config['link_indicator'])
                img_link = res.select(self.config['img_indicator'])

                product = form.formatResult(self.config['site'], title, price, link, img_link)

                if product['title'] != '' and product['price'] != '' and product['link'] != '':
                    products.append(product)

        self.result = products

    def httpsGet(self, URL):
        """makes HTTP called to the requested URL with custom headers

        Parameters
        ----------
        URL: str
            URL we are sending request to

        Returns
        ----------
        soup: str
            HTML of page we requested
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',  # noqa: E501
            'Accept-Encoding': 'gzip, deflate',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '0',
            'Cache-Control': 'no-cache'
        }
        s = requests.Session()
        page = s.get(URL, headers=headers)
        print(f'Page - {URL}. status code {page.status_code}')
        if page.status_code == 200:
            soup1 = BeautifulSoup(page.content, 'html.parser')
            return BeautifulSoup(soup1.prettify(), 'html.parser')
        else:
            print(f'Page - {URL} does not exist with status code {page.status_code}')
            return None


def scrape(args, scrapers):
    """Conduct scraping of sites based on scrapers

    Parameters
    ----------
    args: dict
        Dictionary of arguments used for scraping

        search : str [query to search on]
        sort : str [sort by column name ; pr - price]
        des : boolean [True for reverse, False for asc]
        num : number of rows in the output
    scrapers: list
        List of scrapers to use

    Returns
    ----------
    overall: list
        List of items returned from scrapers
    """
    print('Start Time: ', datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    query = args['search']

    overall = []
    scrapers = sorted(scrapers)

    i = 0
    while i < len(scrapers):
        '''if scrapers[i] == 'amazon':
            t_az = search(query, AMAZON)
            t_az.start()
            i += 1
            if i == len(scrapers):
                break'''
        if scrapers[i] == 'bestbuy':
            t_bb = search(query, BESTBUY)
            t_bb.start()
            i += 1
            if i == len(scrapers):
                break
        if scrapers[i] == 'costco':
            t_ct = search_ct(query, COSTCO)
            t_ct.start()
            i += 1
            if i == len(scrapers):
                break
        if scrapers[i] == 'ebay':
            t_eb = scrape_ebay(query)
            t_eb.start()
            i += 1
            if i == len(scrapers):
                break
        if scrapers[i] == 'target':
            t_tg = scrape_target(query)
            t_tg.start()
            i += 1
            if i == len(scrapers):
                break
        if scrapers[i] == 'walmart':
            t_wm = search(query, WALMART)
            t_wm.start()
            i += 1
            if i == len(scrapers):
                break
        else:
            i += 1
            if i == len(scrapers):
                break

    i = 0
    while i < len(scrapers) :
        '''if scrapers[i] == 'amazon':
            t_az.join()
            i += 1
            for sort_by in args['sort']:
                local = form.sortList(t_az.result, sort_by, args['des'])[:args.get('num', len(t_az.result))]
            overall.extend(local)
            if i == len(scrapers):
                break'''
        if scrapers[i] == 'bestbuy':
            t_bb.join()
            i += 1
            local = t_bb.result
            for sort_by in args['sort']:
                local = form.sortList(local, sort_by, args['des'])[:args.get('num', len(t_bb.result))]
            overall.extend(local)
            if i == len(scrapers):
                break
        if scrapers[i] == 'costco':
            t_ct.join()
            i += 1
            local = t_ct.result
            for sort_by in args['sort']:
                local = form.sortList(local, sort_by, args['des'])[:args.get('num', len(t_ct.result))]
            overall.extend(local)
            if i == len(scrapers):
                break
        if scrapers[i] == 'ebay':
            t_eb.join()
            i += 1
            local = t_eb.result
            for sort_by in args['sort']:
                local = form.sortList(local, sort_by, args['des'])[:args.get('num', len(t_eb.result))]
            overall.extend(local)
            if i == len(scrapers):
                break
        if scrapers[i] == 'target':
            t_tg.join()
            i += 1
            local = t_tg.result
            for sort_by in args['sort']:
                local = form.sortList(local, sort_by, args['des'])[:args.get('num', len(t_tg.result))]
            overall.extend(local)
            if i == len(scrapers):
                break
        if scrapers[i] == 'walmart':
            t_wm.join()
            i += 1
            local = t_wm.result
            for sort_by in args['sort']:
                local = form.sortList(local, sort_by, args['des'])[:args.get('num', len(t_wm.result))]
            overall.extend(local)
            if i == len(scrapers):
                break
        else:
            i += 1
            if i == len(scrapers):
                break


    for sort_by in args['sort']:
        overall = form.sortList(overall, sort_by, args['des'])

    print('Before return time: ', datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    
    return overall
