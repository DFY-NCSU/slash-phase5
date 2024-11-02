import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import src.formattr as formatter
from bs4 import BeautifulSoup

def test_sortList_different_prices():
    """
    Checks sortList with different price values and ordering
    """
    arr = [{"price": "$5"}, {"price": "$15"}, {"price": "$3"}]
    ansArr = [{"price": "$3"}, {"price": "$5"}, {"price": "$15"}]
    revAnsArr = [{"price": "$15"}, {"price": "$5"}, {"price": "$3"}]
    assert formatter.sortList(arr, "pr", False) == ansArr
    assert formatter.sortList(arr, "pr", True) == revAnsArr

def test_sortList_same_prices():
    """
    Checks sortList with identical prices
    """
    arr = [{"price": "$10"}, {"price": "$10"}, {"price": "$10"}]
    ansArr = [{"price": "$10"}, {"price": "$10"}, {"price": "$10"}]
    assert formatter.sortList(arr, "pr", False) == ansArr

# def test_sortList_missing_price_field():
#     """
#     Checks sortList where one dictionary is missing a price field
#     """
#     arr = [{"price": "$10"}, {"price": "$5"}, {}]
#     ansArr = [{}, {"price": "$5"}, {"price": "$10"}]
#     assert formatter.sortList(arr, "pr", False) == ansArr

def test_sortList_mixed_currency_format():
    """
    Checks sortList with mixed currency format in prices
    """
    arr = [{"price": "€10"}, {"price": "$5"}, {"price": "$7"}]
    ansArr = [{"price": "$5"}, {"price": "$7"}, {"price": "€10"}]
    assert formatter.sortList(arr, "pr", False) == ansArr

def test_formatResults_multiple_titles():
    """
    Checks formatResults with multiple title entries
    """
    titles = [
        BeautifulSoup('<div class="title">title 1</div>', "html.parser"),
        BeautifulSoup('<div class="title">title 2</div>', "html.parser")
    ]
    prices = [BeautifulSoup('<div class="price">$1.99</div>', "html.parser")]
    links = []
    images = []
    product = formatter.formatResult("example", titles, prices, links, images)
    assert product["title"] == "title 1"

# def test_formatResults_no_price():
#     """
#     Checks formatResults with no price entry
#     """
#     titles = [BeautifulSoup('<div class="title">Sample Title</div>', "html.parser")]
#     prices = []
#     links = []
#     images = []
#     product = formatter.formatResult("example", titles, prices, links, images)
#     assert product["price"] == "N/A"

def test_formatResults_special_characters_title():
    """
    Checks formatResults with special characters in title
    """
    titles = [BeautifulSoup('<div class="title">Special & Char Title</div>', "html.parser")]
    prices = [BeautifulSoup('<div class="price">$2.50</div>', "html.parser")]
    links = []
    images = []
    product = formatter.formatResult("example", titles, prices, links, images)
    assert product["title"] == "Special & Char Title"

# def test_formatResults_empty_title():
#     """
#     Checks formatResults with an empty title entry
#     """
#     titles = [BeautifulSoup('<div class="title"></div>', "html.parser")]
#     prices = [BeautifulSoup('<div class="price">$0.99</div>', "html.parser")]
#     links = []
#     images = []
#     product = formatter.formatResult("example", titles, prices, links, images)
#     assert product["title"] == "N/A"

# def test_formatResults_incomplete_data():
#     """
#     Checks formatResults with incomplete data for product
#     """
#     titles = [BeautifulSoup('<div class="title">Incomplete Data</div>', "html.parser")]
#     prices = []
#     links = [BeautifulSoup('<a href="http://example.com">link</a>', "html.parser")]
#     images = []
#     product = formatter.formatResult("example", titles, prices, links, images)
#     assert product["price"] == "N/A" and product["title"] == "Incomplete Data"

def test_sortList_empty_array():
    """
    Checks sortList with an empty array input
    """
    arr = []
    assert formatter.sortList(arr, "pr", False) == []
