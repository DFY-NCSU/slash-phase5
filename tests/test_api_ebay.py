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


def test_api_ebay():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    assert results is not None


def test_api_ebay1():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    assert len(results) > 0


def test_api_ebay2():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    assert len(results) == 10


def test_api_ebay3():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    assert isinstance(results, list)


def test_api_ebay4():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    assert isinstance(results[0], dict)


def test_api_ebay5():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    for result in results:
        assert 'price' in result


def test_api_ebay6():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    for result in results:
        assert 'link' in result


def test_api_ebay7():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    for result in results:
        assert 'img_link' in result

def test_api_ebay8():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    for result in results:
        assert 'title' in result


def test_api_ebay9():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    for result in results:
        assert 'timestamp' in result


def test_api_ebay_collected_produce_price():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    prices = [result['price'] for result in results]

    for price in prices:
        assert check_price(price)


def test_api_ebay_collected_produce_title():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    titles = [result['title'] for result in results]

    for title in titles:
        assert title != ''


def test_api_ebay_collected_produce_link():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    links = [result['link'] for result in results]

    for link in links:
        # assert is a link
        assert link.startswith('http') or link.startswith('https') or link.startswith('www')


def test_api_ebay_collected_produce_img_link():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    img_links = [result['img_link'] for result in results]

    for img_link in img_links:
        # assert is a link
        assert img_link.startswith('http') or img_link.startswith('https') or img_link.startswith('www')


def test_api_ebay_collected_produce_timestamp():
    product = 'lenovo'
    site = 'eb'
    results = search_items_API(site, product)
    timestamps = [result['timestamp'] for result in results]

    for timestamp in timestamps:
        assert timestamp != ''