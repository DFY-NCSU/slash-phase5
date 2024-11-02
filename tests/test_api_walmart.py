# -*- coding: utf-8 -*-
"""
Created on Tue Oct. 01 17:17:17 2024

@author: Sen Fng
"""

import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from src.main_streamlit import search_items_API


def check_price(price):
    price = price.replace('$', '')
    try:
        price = float(price)
        return True
    except ValueError:
        return False


def test_api_walmart():
    """Assert that the API returns a list of items"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    assert results is not None


def test_api_walmart1():
    """Assert that the API returns a list of items"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    assert len(results) > 0


def test_api_walmart2():
    """Assert that the API returns a list of items (9 items)"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    assert  len(results) == 9


def test_api_walmart3():
    """Assert that the API returns a list of items"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    assert isinstance(results, list)


def test_api_walmart4():
    """Assert that the API returns a list of items with dictionary"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    assert isinstance(results[0], dict)


def test_api_walmart5():
    """Assert that the API returns a list of items with dictionary, and the dictionary has a title key"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    assert 'title' in results[0]


def test_api_walmart6():
    """Assert that the API returns a list of items with dictionary, and the dictionary has a price key"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    assert 'price' in results[0]


def test_api_walmart7():
    """Assert that the API returns a list of items with dictionary, and the dictionary has a link key"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    assert 'link' in results[0].keys()


def test_api_walmart8():
    """Assert that the API returns a list of items with dictionary, and the dictionary has a timestamp key"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    assert 'timestamp' in results[0].keys()


def test_api_walmart9():
    """Assert that the API returns a list of items with dictionary, and the dictionary has a img_link key"""
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    assert 'img_link' in results[0]


def test_api_walmart_collected_produce_price():
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    prices = [result['price'] for result in results]

    for price in prices:
        assert check_price(price)


def test_api_walmart_collected_produce_title():
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    titles = [result['title'] for result in results]

    for title in titles:
        assert title != ''


def test_api_walmart_collected_produce_link():
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    links = [result['link'] for result in results]

    for link in links:
        # assert is a link
        assert link.startswith('http') or link.startswith('https') or link.startswith('www')


def test_api_walmart_collected_produce_img_link():
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    img_links = [result['img_link'] for result in results]

    for img_link in img_links:
        # assert is a link
        assert img_link.startswith('http') or img_link.startswith('https') or img_link.startswith('www')


def test_api_walmart_collected_produce_timestamp():
    product = 'laptop'
    site = 'wm'
    results = search_items_API(site, product)
    timestamps = [result['timestamp'] for result in results]

    for timestamp in timestamps:
        # assert is a timestamp
        assert timestamp != ''
