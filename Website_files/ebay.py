from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def check_ebay_account(email):
    driver = webdriver.Firefox()

    driver.get("https://signin.ebay.com/")

    driver.implicitly_wait(10)
    email_feild = driver.find_element(By.XPATH, '//*[@id="userid"]')
    email_feild.send_keys(email)

    email_feild_button = driver.find_element(By.XPATH, '//*[@id="signin-continue-btn"]')
    email_feild_button.click()

    try:
        time.sleep(5)
        not_found_log = driver.find_element(By.XPATH, '//*[@id="signin-error-msg"]')
        not_found_log_text = not_found_log.text

        driver.close()

        if not_found_log_text == 'We couldn\'t find this eBay account.':
            return False
        return True

    except NoSuchElementException:
        driver.close()
        return "Error"


