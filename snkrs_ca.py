import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

UPCOMING_RELEASES = "https://www.nike.com/ca/launch?s=upcoming"
EARLY_LINK = ""
RELEASE_TITLE = ""


def capsule_toronto_main(PATH):
    EMAIL = str(input("enter email:\n"))
    PASSWORD = str(getpass.getpass("\nenter password:\n"))
    driver = webdriver.Chrome(PATH)
    
    driver.find_element_by_id("CustomerEmail").send_keys(EMAIL)
    driver.find_element_by_id("CustomerPassword").send_keys(PASSWORD)
    driver.find_element_by_xpath("//input[@type='submit']").click()
    # idle 60s to solve capcha
    time.sleep(60)
    driver.refresh()
    driver.maximize_window()
    driver.get(NEW_ARRIVAL_LINK)
    boo = True
    # monitor + auto check out starts
    while boo:
        try:
            driver.find_element_by_css_selector(
                "a[href*='"+str(keywords)+"']").click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//label[@for="swatch-0-' + str(size) + '"]'))).click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.ID, "AddToCartText-product-template"))).click()
            # Covid Agreement
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.ID, "agree"))).click()
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "checkout"))).click()
            boo = False
        except:
            driver.refresh()
    time.sleep(600)
