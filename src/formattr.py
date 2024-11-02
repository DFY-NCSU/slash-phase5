"""
Copyright (c) 2021 Rohan Shah
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Slash
"""

from datetime import datetime
import math
import html

"""
The formatter module focuses on processing raw text and returning it in
the required format.
"""


def formatResult(website, titles, prices, links, img_link):
    """
    The formatResult function takes the scraped HTML as input, and extracts the
    necessary values from the HTML code. Ex. extracting a price '$19.99' from
    a paragraph tag.
    """
    title, price, link = '', '', ''
    if titles:
        title = titles[0].get_text().strip()
    if prices:
        if website == "walmart" or website == "ebay":
            price = prices
        else:
            price = prices[0].get_text().strip()
    if links:
        link = links[0]['href']
    if img_link:
        img_link = img_link[0]['src']
    product = {
        'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "title": formatTitle(title),
        "price": price,
        "link": f'www.{website}.com{link}',
        "img_link": img_link,
        "website": website,
    }
    if website=='walmart':
        if link[0:4]=='http':
            product['link']=f'{link}'
    if website == 'costco':
        product['link'] = f'{link}'
    return product


def formatResultBestBuy(website, titles, prices, links, img_link):
    """
    The formatResult function takes the scraped HTML as input, and extracts the
    necessary values from the HTML code. Ex. extracting a price '$19.99' from
    a paragraph tag.
    """
    title, price, link = '', '', ''
    # Process title
    title = titles.strip() if isinstance(titles, str) else (titles[0].get_text(strip=True) if hasattr(titles[0], 'get_text') else '')

    # Process link
    if isinstance(links, str):
        link = links
    elif hasattr(links[0], 'get'):
        link = links[0].get('href', '')
    else:
        link = ''
    
    # Process image link
    img_link = img_link[0]['src'] if hasattr(img_link[0], 'get') else img_link if isinstance(img_link, str) else ''
    if prices:
        # price = prices[0].get_text().strip()
        price = prices
    product = {
        'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "title": formatTitle(title),
        "price": price,
        "link": f'www.{website}.com{link}',
        "img_link": img_link,
        "website": website,
    }
    if website=='walmart':
        if link[0:4]=='http':
            product['link']=f'{link}'
    if website == 'costco':
        product['link'] = f'{link}'
    return product


def formatResultCostco(website, product):
    """
    This function formats the results from the Costco scraper. Since we use different operation flow for Costco,
    we need to format the results differently.
    param: 
        website: str: The website name
        product: dict: The product dictionary contains parts of product information
    return:
        product: dict: The formatted product dictionary with full product information
    """

    # add timestamp
    product['timestamp'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # add website
    product['website'] = website

    return product


def sortList(arr, sortBy, reverse):
    """
    The sortList function is used to sort the products list based on the
    flags provided as args. Currently, it supports sorting by price.
    """
    if sortBy == "pr":
        return sorted(arr, key=lambda x: getNumbers(x["price"]), reverse=reverse)
    # To-do: sort by rating
    elif sortBy == "ra":
        # return sorted(arr, key=lambda x: getNumbers(x.price), reverse=reverse)
        pass
    return arr


def formatSearchQuery(query):
    """
    The formatSearchQuery function formats the search string into a string that
    can be sent as a url paramenter.
    """
    return query.replace(" ", "+")


def formatSearchQueryForCostco(query):
    """
    The formatSearchQueryForCostco function formats the search string into a string that
    can be sent as a url paramenter.
    """
    queryStrings = query.split(' ')
    formattedQuery = ""
    for str in queryStrings:
        formattedQuery += str
        formattedQuery += '+'
    formattedQuery = formattedQuery[:-1]
    return formattedQuery


def formatTitle(title):
    """
    The formatTitle function formats titles extracted from the scraped HTML code.
    """
    title = html.unescape(title)
    if(len(title) > 40):
        return title[:40] + "..."
    return title


def getNumbers(st):
    """
    The getNumbers function extracts float values (price) from a string.
    Ex. it extracts 10.99 from '$10.99' or 'starting at $10.99'
    """
    ans = ''
    for ch in st:
        if (ch >= '0' and ch <= '9') or ch == '.':
            ans += ch
    try:
        ans = float(ans)
    except:  # noqa: E722
        ans = math.inf
    return ans
