# Code Description

## Website Function & RedCircle API

### 1. `src/main_streamlit.py`

Main file for Streamlit website.

### 2. `src/main.py`

Main file for RedCircle API endpoints.

### 3. `src/scraper.py`

Contains methods to scrape individual websites to retrieve searched items.

### 4. `src/scraper_mt.py`

Includes a method for crawling a shopping site using a multi-threaded static crawler to retrieve items on demand, with performance better than `scraper.py`.

### 5. `src/configs.py`

Contains the configurations for website scrapers.

### 6. `src/configs_mt.py`

Includes configuration and methods for a multi-threaded web scraper and the addition of a target dynamic crawler.

### 7. `src/url_shortener.py`

Contains method to shorten large URLs using the `pyshorteners` ([tiny.cc](http://tiny.cc/)) API.

### 8. `src/formattr.py`

Contains additional utility methods for formatting search queries, URLs, results, and other text. Also adds Bestbuy's formatted search function.

### 9. `src/currency_converter.py`

Contains a function that converts the price from USD to user-preferred currency using the `CurrencyConverter` library.

### 10. `src/database.py`

Sets up a PostgreSQL database connection using SQLAlchemy, including the definition of a session and declarative base for ORM operations.

### 11. `src/models.py`

Defines models for the database tables used in ORM operations in the application.

### 12. `src/pages/login.py`

Creates a Streamlit login page that facilitates user authentication via username and password.

### 13. `src/pages/logout.py`

Contains a method to log out the currently logged-in user.

### 14. `src/pages/register.py`

Creates a Streamlit registration page to facilitate user registration.

### 15. `src/pages/search.py`

Allows users to search for products from various websites, display search results based on criteria like price range, cheapest product, and add selected items to a wishlist.

### 16. `src/pages/wishlist.py`

Displays the wishlist for the logged-in user. The code has a two-column layout to display products properly. A link to the latest product added to the wishlist is displayed on top of all wishlist products.

### 17. `src/routers/auth.py`

Contains API endpoints for user authentication, access token management, and user registration, with secure hashing and validation.

### 18. `src/routers/wish_list.py`

Contains API endpoints for managing a user's wishlist, allowing users to add, view, and remove items from their wishlist.

### 19. `tests/tests_api_bestbuy.py`

Test case for crawling the bestbuy web crawler functionality

### 20.`tests/tests_api_target_new.py`

Test case for crawling the target web crawler functionality

### 21.`tests/formatNumber_new.py`

Test cases for whether the crawler function is able to fetch the content properly

### 22.`tests/formatResults_new.py`

Test cases for whether the content returned by the crawler is formatted or not

### 23.`tests/tests_api_general.py`

General Test case for crawling the all web crawler functionality

### 24.`tests/tests_api_walmart.py`

Test case for crawling the walmart web crawler functionality

### 25.`tests/tests_formatText.py`

Test cases for whether the queries and titles returned by the crawler are formatted or not