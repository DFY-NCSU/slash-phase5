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
    
def test_api_general_sort():
    # Tests the sorting functionality of search_items_API with ascending price order.
    product = 'laptop'
    site = 'all'
    results = search_items_API(site, product, order_by_col='price')
    prices = [float(result['price'].replace('$', '').replace(',', '')) for result in results]
    assert prices == sorted(prices)
    
def test_api_general_reverse_sort():
    # Tests the sorting functionality of search_items_API with descending price order.
    product = 'laptop'
    site = 'all'
    results = search_items_API(site, product, order_by_col='price', reverse=True)
    prices = [float(result['price'].replace('$', '').replace(',', '')) for result in results]
    assert prices == sorted(prices, reverse=True)