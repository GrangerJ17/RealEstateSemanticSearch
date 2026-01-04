import requests
import re
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import httpx
from bs4 import BeautifulSoup

# assumptions: 
# - css selector and class names are known before use script (a function will be given to extract them)
# - then you can target these classes and extract from them



# TODO: pull ordered tags, read from tags given by user once they are known, extract data into user defined fields, bypass/handle logins


url = "https://www.linkedin.com.au/jobs/"

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options) 


driver.get(url)
elements = driver.find_elements("xpath", "//*[@class]")

classes = set()
for el in elements:
    for cls in el.get_attribute("class").split():
        classes.add(cls)

print(sorted(classes))

driver.quit()