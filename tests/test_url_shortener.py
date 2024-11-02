import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from src.url_shortener import shorten_url

def test_url_shortener():
    url = 'https://www.bestbuy.com/site/dell-inspiron-7000-2-in-1-13-3-fhd-touch-screen-laptop-intel-core-i5-8gb-memory-512gb-ssd-32gb-optane-silver/6432548.p?skuId=6432548'
    s_url = shorten_url(url)
    assert 'tinyurl.com' in s_url