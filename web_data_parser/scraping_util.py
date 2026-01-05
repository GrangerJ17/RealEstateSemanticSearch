from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def click_all_load_more(driver, button_selector, timeout=5):
    """
    Clicks all buttons on the page until none are left.
    """
    last_height = None
    while True:
        
        
        try:
            button = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector))
            )
            button.click()
            # optional: wait a bit for content to load
            WebDriverWait(driver, timeout).until(lambda d: True)
            
            new_height = scroll_to_bottom(driver)
            if last_height and last_height == new_height:
                break

            last_height = new_height
        except TimeoutException:
            # no more button found, exit loop
            break

def scroll_to_bottom(driver, pause=1, max_scrolls=50):
    """
    Scrolls the page to bottom repeatedly to trigger lazy-loading.
    """
    last_height = driver.execute_script("return document.body.scrollHeight")
    for _ in range(max_scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # reached bottom
        last_height = new_height
    
    return last_height


