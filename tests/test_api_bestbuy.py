# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 2024

@author: Weiyuan Ding
"""

import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from src.main_streamlit import search_items_API

def check_price(price):
    # Removes the dollar sign from the price string and attempts to convert it to a float
    # Returns True if successful, False if a ValueError is raised (indicating invalid price format)
    price = price.replace('$', '')
    try:
        price = float(price)
        return True
    except ValueError:
        return False

def test_api_bestbuy():
    # Checks if the search_items_API function returns any result for the product 'laptop' from Best Buy ('bb')
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    assert results is not None

def test_api_bestbuy1():
    # Verifies that the search_items_API function returns a non-empty list of results for 'laptop' from Best Buy
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    assert len(results) > 0

def test_api_bestbuy2():
    # Ensures that exactly 10 results are returned by search_items_API for 'laptop' from Best Buy
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    assert len(results) == 10

def test_api_bestbuy3():
    # Confirms that the results returned by search_items_API are in list format
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    assert isinstance(results, list)

def test_api_bestbuy4():
    # Verifies that each item in the results list is a dictionary
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    assert isinstance(results[0], dict)

def test_api_bestbuy5():
    # Checks that each result dictionary contains a 'timestamp' key
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    assert 'timestamp' in results[0].keys()

def test_api_bestbuy6():
    # Ensures that each result dictionary has a 'title' key
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    assert 'title' in results[0].keys()

def test_api_bestbuy7():
    # Confirms that each result dictionary includes a 'price' key
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    assert 'price' in results[0].keys()

def test_api_bestbuy8():
    # Checks that each result dictionary includes a 'link' key
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    assert 'link' in results[0].keys()

def test_api_bestbuy9():
    # Verifies that each result dictionary contains an 'img_link' key for the product image URL
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    assert 'img_link' in results[0].keys()

def test_api_bestbuy10():
    # Confirms that each result dictionary includes a 'website' key indicating the source site
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    assert 'website' in results[0].keys()

def test_api_bestbuy_collected_produce_price():
    # Checks that each result's 'price' value is in a valid numeric format by calling check_price function
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    for result in results:
        assert check_price(result['price'])

def test_api_bestbuy_collected_produce_title():
    # Ensures that each result's 'title' value is not an empty string
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    for result in results:
        assert result['title'] != ""

def test_api_bestbuy_collected_produce_link():
    # Verifies that each result's 'link' value is a valid URL starting with 'http', 'https', or 'www'
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    for result in results:
        link = result['link']
        assert link.startswith('http') or link.startswith('https') or link.startswith('www')

def test_api_bestbuy_collected_produce_img_link():
    # Ensures that each result's 'img_link' value is a valid URL starting with 'http', 'https', or 'www'
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    for result in results:
        img_link = result['img_link']
        assert img_link.startswith('http') or img_link.startswith('https') or img_link.startswith('www')

def test_api_bestbuy_collected_produce_timestamp():
    # Confirms that each result's 'timestamp' value is not an empty string
    product = 'laptop'
    site = 'bb'
    results = search_items_API(site, product)
    for result in results:
        assert result['timestamp'] != ""

def test_api_bestbuy_null():
    product = ''
    site = 'bb'
    results = search_items_API(site, product)
    assert results is None
    
def test_api_bestbuy_mojibake():
    product = '!@#$%^&*()'
    site = 'bb'
    results = search_items_API(site, product)
    assert results is None
