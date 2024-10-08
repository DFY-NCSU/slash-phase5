"""
Copyright (c) 2021 Rohan Shah
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Slash
"""

# package imports
from bs4 import BeautifulSoup
import requests
from datetime import datetime


# local imports
import src.formattr as form
# from src.configs import AMAZON, WALMART, COSTCO, BESTBUY, scrape_ebay, scrape_target
from src.configs import WALMART, BESTBUY, scrape_ebay, scrape_target

def httpsGet(URL):
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
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'no-cache'
    }
    s = requests.Session()
    page = s.get(URL, headers=headers)
    if page.status_code == 200:
        soup1 = BeautifulSoup(page.content, 'html.parser')
        return BeautifulSoup(soup1.prettify(), 'html.parser')
    else:
        # TODO add logger
        return None


def search(query, config):
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
    if config['site'] == 'costco':
        query = form.formatSearchQueryForCostco(query)
    else:
        query = form.formatSearchQuery(query)
    URL = config['url'] + query

    # fetch url
    page = httpsGet(URL)
    if not page:
        return []

    # begin parsing page content
    results = page.find_all(config['item_component'], config['item_indicator'])
    products = []
    for res in results:
        title = res.select(config['title_indicator'])
        price = res.select(config['price_indicator'])
        link = res.select(config['link_indicator'])
        product = form.formatResult(config['site'], title, price, link)
        if product['title'] != '':
            products.append(product)
    return products


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
    for scraper in scrapers:
        if scraper == 'walmart':
            local = search(query, WALMART)
        # elif scraper == 'amazon':
            # local = search(query, AMAZON)
        elif scraper == 'target':
            local = scrape_target(query)
        elif scraper == 'ebay':
            local = scrape_ebay(query)
        # elif scraper == 'costco':
            # local = search(query, COSTCO)
        elif scraper == 'bestbuy':
            local = search(query, BESTBUY)
        else:
            continue
        # TBD : move number of items fetched to global level ?
        for sort_by in args['sort']:
            local = form.sortList(local, sort_by, args['des'])[:args.get('num', len(local))]
        overall.extend(local)

    for sort_by in args['sort']:
        overall = form.sortList(overall, sort_by, args['des'])

    print('Before return time: ', datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    
    return overall
