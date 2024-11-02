from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from threading import Thread
from time import sleep

import src.formattr as form


class search_ct(Thread):
    def __init__(self, query, config):
        self.result: dict = None
        self.query = query
        self.config = config
        super(search_ct, self).__init__()

    # Setup Chrome driver with options
    def setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        ua = UserAgent()
        user_agent = ua.random
        chrome_options.add_argument(f'user-agent={user_agent}')
        driver = webdriver.Chrome(options=chrome_options)
        return driver
        
    def run(self):
        """Scrape the given config for a specific item

        Parameters
        ----------
        query: str
            Query of item we are looking for
        config: dict
            Configuration for site we are scraping

        Returns
        ----------
        products: list
            List of items returned from website
        """
        self.query = form.formatSearchQuery(self.query)
        URL = self.config['url'] + self.query

        # fetch url
        driver = self.setup_driver()
        driver.get(URL)

        self.load_full_page(driver)

        self.result = self.scrape_products(driver)

    # Function to scroll and wait for products to load
    def load_full_page(self, driver):
        SCROLL_PAUSE_TIME = 2
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to the bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(SCROLL_PAUSE_TIME)
            
            # Wait for product titles or price elements to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "price"))
            )
            
            # Check if the scroll height has changed
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    # Scrape product information
    def scrape_products(self, driver):
        results = []
        products = []
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Find all product containers
        product_elements = soup.find_all('div', class_='product-tile-set')

        for product in product_elements:
            # Find title within the product element
            title_tag = product.find('span', class_='description') or product.find('p', class_='description')
            title_text = title_tag.get_text(strip=True) if title_tag else 'N/A'

            # Find price within the product element
            price_tag = product.find('div', class_='price')
            price_text = price_tag.get_text(strip=True) if price_tag else 'N/A'

            # Find product link
            link_tag = product.find('a', href=True)
            if link_tag and link_tag['href']:
                # Costco links might be relative, so prepend the base URL if needed
                product_link = link_tag['href']
                if not product_link.startswith('http'):
                    product_link = 'https://www.costco.com' + product_link
            else:
                product_link = 'N/A'

            # Find product image
            img_tag = product.find('img')
            if img_tag:
                # Image URL might be in 'src' or 'data-src' attribute
                product_image = img_tag.get('src') or img_tag.get('data-src') or 'N/A'
                if product_image.startswith('//'):
                    # Add 'https:' to URLs that start with '//'
                    product_image = 'https:' + product_image
            else:
                product_image = 'N/A'

            results.append({
                'title': title_text,
                'price': price_text,
                'link': product_link,
                'img_link': product_image
            })
        
        # format product information
        for result in results:
            product = form.formatResultCostco(self.config['site'], result)
            products.append(product)

        return products
    

if __name__ == '__main__':
    query = 'laptop'
    config = {
        'url': 'https://www.costco.com/CatalogSearch?dept=All&keyword=',
        'site': 'costco',
        'title_indicator': ['span', {'class': 'description'}],
        'price_indicator': ['div', {'class': 'price'}],
        'link_indicator': ['a', {'class': 'product-link'}],
        'img_indicator': ['img', {'class': 'product-image'}]
    }
    scraper = search_ct(query, config)
    scraper.start()
    scraper.join()
    # print(scraper.result)
    results = scraper.result[:10] if scraper.result else []
    for result in results:
        print(result)

