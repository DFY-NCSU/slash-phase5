import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import src.formattr as formatter
import math

def test_getNumbers_special_chars():
    """Checks getNumbers with special characters surrounding the number"""
    assert formatter.getNumbers("### $15.75 !!!") == 15.75
    assert formatter.getNumbers("@@ $$12.50 %%") == 12.50

# def test_getNumbers_no_dollar_sign():
#     """Checks getNumbers without a dollar sign"""
#     assert formatter.getNumbers("Total is 20.00 dollars") == math.inf

# def test_getNumbers_multiple_numbers():
#     """Checks getNumbers with multiple dollar amounts"""
#     assert formatter.getNumbers("Total $5.00 and $7.50") == 5.00

# def test_getNumbers_negative_value():
#     """Checks getNumbers with a negative dollar amount"""
#     assert formatter.getNumbers("Loss of $-10.00") == -10.00

def test_getNumbers_no_numeric_value():
    """Checks getNumbers with text but no numeric value"""
    assert formatter.getNumbers("Price is $") == math.inf

def test_getNumbers_large_number():
    """Checks getNumbers with a large dollar amount"""
    assert formatter.getNumbers("Cost is $1000000.99") == 1000000.99

# def test_getNumbers_currency_symbol_variation():
#     """Checks getNumbers with other currency symbols"""
#     assert formatter.getNumbers("Amount is €50.00") == math.inf

def test_getNumbers_decimal_without_zero():
    """Checks getNumbers with a decimal amount lacking leading zero"""
    assert formatter.getNumbers("Amount is $.99") == 0.99

# def test_getNumbers_multiple_currency_symbols():
#     """Checks getNumbers with multiple currency symbols in the text"""
#     assert formatter.getNumbers("Total cost is $30.00 and £20.00") == 30.00

def test_getNumbers_no_spaces():
    """Checks getNumbers with no spaces between text and dollar amount"""
    assert formatter.getNumbers("Amount:$25.50") == 25.50

