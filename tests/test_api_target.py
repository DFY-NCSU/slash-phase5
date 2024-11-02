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


def test_api_target():
    # Check we can get value
    product = 'dell'
    product = 'laptop'
    site = 'tg'
    result = search_items_API(site, product)
    assert result is not None


def test_item_existance():
    # Check if the item is exist
    product = 'dell'
    site = 'tg'
    result = search_items_API(site, product)
    for i in range(len(result)):
        assert result[i] is not None


def test_price_existance():
    # Check if the price is exist
    product = 'dell'
    site = 'tg'
    result = search_items_API(site, product)
    for i in range(len(result)):
        assert 'price' in result[i]


def test_time_existance():
    #Check if the time is exist
    product = 'dell'
    site = 'tg'
    result = search_items_API(site, product)
    for i in range(len(result)):
        assert 'timestamp' in result[i]


def test_link_existance():
    #Check if the link is exist
    product = 'dell'
    site = 'tg'
    result = search_items_API(site, product)
    for i in range(len(result)):
        assert 'link' in result[i]


def test_title_existance():
    #Check if the title is exist
    product = 'dell'
    site = 'tg'
    result = search_items_API(site, product)
    for i in range(len(result)):
        assert 'title' in result[i]


def test_item_info_length():
    #Check the length of the item_info
    product = 'dell'
    site = 'tg'
    result = search_items_API(site, product)
    for i in range(len(result)):
        assert len(result[i]) == 4


def test_price_correctness():
    # Check the price correctness
    product = 'dell'
    site = 'tg'
    result = search_items_API(site, product)
    for i in range(len(result)):
        assert result[i]['price'] >= 0


def test_link_http():
    # Check if the link is http
    product = 'dell'
    site = 'tg'
    result = search_items_API(site, product)
    for i in range(len(result)):
        assert result[i]['link'][:4] == "http"

def test_price_length():
    #Check the length of the price
    product = 'dell'
    site = 'tg'
    result = search_items_API(site, product)
    for i in range(len(result)):
        assert result[i]['price'] > 0


def test_seller_rating_range():
    #Check the seller rating
    product = 'dell'
    site = 'tg'
    result = search_items_API(site, product)
    for i in range(len(result)):
        assert 0 <= result[i].get('seller_rating', 0) <= 5


def test_discount_value():
    # Check the discount value
    product = 'dell'
    site = 'tg'
    result = search_items_API(site, product)
    for i in range(len(result)):
        discount = result[i].get('discount', 0)
        assert discount >= 0


def test_isinstance():
    # Verifies that each item in the results list is a dictionary
    product = 'dell'
    site = 'tg'
    results = search_items_API(site, product)
    assert isinstance(results[0], dict)

def test_list_format():
    product = 'dell'
    site = 'tg'
    results = search_items_API(site, product)
    assert isinstance(results, list)

def test_collected_produce_title():
    # Checks that each result's 'title' value is in a valid numeric format by calling check_price function
    product = 'dell'
    site = 'tg'
    results = search_items_API(site, product)
    for result in results:
        assert result['title'] != ""

def test_collected_produce_timestamp():
    # Checks that each result's 'timestamp' value is in a valid numeric format by calling check_price function
    product = 'dell'
    site = 'tg'
    results = search_items_API(site, product)
    for result in results:
        assert result['timestamp'] != ""

def test_collected_produce_price():
    # Checks that each result's 'price' value is in a valid numeric format by calling check_price function
    product = 'dell'
    site = 'tg'
    results = search_items_API(site, product)
    for result in results:
        assert result['price'] != ""

def test_target_results():
    # Ensures that exactly 10 results are returned by search_items_API for 'laptop' from target
    product = 'dell'
    site = 'tg'
    results = search_items_API(site, product)
    assert len(results) == 10

def test_have_more_results():
    # Ensures that there have results are returned by search_items_API for 'laptop' from target
    product = 'dell'
    site = 'tg'
    results = search_items_API(site, product)
    assert len(results) >0

def check_price(price):
    # Removes the dollar sign from the price string and attempts to convert it to a float
    # Returns True if successful, False if a ValueError is raised (indicating invalid price format)
    price = str(price).replace('$', '')
    try:
        price = float(price)
        return True
    except ValueError:
        return False

def test_checkprice_format():
    # Checks that each result's 'price' value is in a valid numeric format by calling check_price function
    product = 'dell'
    site = 'tg'
    results = search_items_API(site, product)
    for result in results:
        assert check_price(result['price'])





