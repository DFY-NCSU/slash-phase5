# -*- coding: utf-8 -*-
"""
Created on Wed Oct. 30 2024

@author: Sen Fang
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
    price = price.replace(',', '')
    try:
        price = float(price)
        return True
    except ValueError:
        return False


def test_api_costco():
    """Assert that the API returns a list of items"""
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    assert isinstance(result, list)


def test_api_costco1():
    """Assert that the API returns a list of items"""
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    assert len(result) > 0 and len(result) == 24


def test_api_costco2():
    """Assert that the API returns a list of items with dictionary"""
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    assert isinstance(result[0], dict)


def test_api_costco3():
    """Assert that the API returns a list of items with dictionary, and the dictionary has a title key"""
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    assert 'title' in result[0]


def test_api_costco4():
    """Assert that the API returns a list of items with dictionary, and the dictionary has a price key"""
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    assert 'price' in result[0]


def test_api_costco5():
    """Assert that the API returns a list of items with dictionary, and the dictionary has a website key"""
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    assert 'website' in result[0]


def test_api_costco6():
    """Assert that the API returns a list of items with dictionary, and the dictionary has a link key"""
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    assert 'link' in result[0]


def test_api_costco7():
    """Assert that the API returns a list of items with dictionary, and the dictionary has a link key"""
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    assert 'img_link' in result[0]


def test_api_costco8():
    """Assert that the API returns a list of items with dictionary, and the dictionary has a timestamp key"""
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    assert 'timestamp' in result[0]


def test_api_costco_collected_produce_price():
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    prices = [item['price'] for item in result]
    assert all([check_price(price) for price in prices])


def test_api_costco_collected_produce_title():
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    titles = [item['title'] for item in result]
    assert all([title != '' for title in titles])


def test_api_costco_collected_produce_link():
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    links = [item['link'] for item in result]
    assert all([link != '' for link in links])


def test_api_costco_collected_produce_img_link():
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    img_links = [item['img_link'] for item in result]
    assert all([img_link != '' for img_link in img_links])


def test_api_costco_collected_produce_website():
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    websites = [item['website'] for item in result]
    assert all([website == 'costco' for website in websites])


def test_api_costco_collected_produce_timestamp():
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product)
    timestamps = [item['timestamp'] for item in result]
    assert all([timestamp != '' for timestamp in timestamps])


def test_api_costco_collected_produce_order():
    product = 'laptop'
    site = 'ct'
    result = search_items_API(site, product, order_by_col='price')
    prices = [item['price'] for item in result]
    assert all(prices[i] <= prices[i + 1] for i in range(len(prices) - 1))