from selenium import webdriver
from scraping_util import scroll_to_bottom, click_all_load_more
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from clean_data import *
from store_data import write_to_csv
import time
import json
import pprint

options = Options()
options.add_argument("--headless")  
options.add_argument("--disable-gpu")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "file:///Users/jamesgranger/data_admin_toolkit/web_data_parser/test.html"  # Or hosted URL

wait_for_selectors = [
    ".product-card",           # Wait for products to load
    ".product-title",          # Ensure titles are present
]

button_selectors = [
    "#loadMoreBtn"             # Click "Load More" button
]

# Selector map - maps CSS selectors to field names
selector_map = {
    # Basic product info
    ".product-title": "title",
    ".product-price": "price",
    ".product-stock": "stock",
    ".product-description": "description",
    
    # Ratings
    ".product-rating": "rating",
    
    # Specifications (nested data)
    ".spec-item[data-spec='brand']": "brand",
    ".spec-item[data-spec='processor']": "processor",
    ".spec-item[data-spec='ram']": "ram",
    ".spec-item[data-spec='storage']": "storage",
    ".spec-item[data-spec='resolution']": "resolution",
    ".spec-item[data-spec='refresh']": "refresh_rate",
    
    # Tags (multiple per product)
    ".tag": "tags",
    
    # Seller info
    ".seller-name": "seller",
    ".product-sku": "sku",
}

# Run the scraper
soup = fetch_html_with_js(
    driver, 
    url, 
    wait_for_selectors=wait_for_selectors,
    scroll=True,
    button=button_selectors
)

extracted = extract_fields(soup, selector_map)
cleaned = clean_data(extracted)

csv = write_to_csv(cleaned, "./extracted_csvs/test_ecom.csv")

print(csv)

driver.quit()
