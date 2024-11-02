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

def test_api_general_invalid_site():
    # Tests the behavior of search_items_API with an invalid site parameter.
    product = 'laptop'
    site = 'unknown'
    results = search_items_API(site, product)
    assert results is None
    
def test_api_general_all_sites():
    # Tests search_items_API with 'all' as the site parameter, expecting it to query all available sites.
    product = 'laptop'
    site = 'all'
    results = search_items_API(site, product)
    results_sites = set()
    for result in results:
        results_sites.add(result['website'])
    assert results_sites == {'walmart', 'ebay', 'bestbuy'}
