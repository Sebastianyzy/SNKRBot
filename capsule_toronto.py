import selenium
import time
import getpass
import bypass_reCapcha
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

UPCOMING_RELEASES = "https://www.capsuletoronto.com/pages/launches"
EARLY_LINK = "https://www.capsuletoronto.com/products/"
LOG_IN = "https://www.capsuletoronto.com/account"
NEW_ARRIVAL_LINK = "https://www.capsuletoronto.com/collections/new-arrivals"
RELEASE_TITLE = "address"


def capsule_toronto_main(PATH):
    EMAIL = str(input("enter email:\n"))
    PASSWORD = str(getpass.getpass("\nenter password:\n"))
    keywords = str(input("\nenter search keywords:\n"))
    size = str(input("\nenter size:\n"))
    size = size.replace(".", "-") if "." in size else size
    print("\nrunning...")
    driver = webdriver.Chrome(PATH)
    driver.get(LOG_IN)
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


def capsule_toronto_pull_calendar(driver, link, calendar):
    driver.get(link)
    release_blog = driver.find_elements_by_class_name(RELEASE_TITLE)
    for shoes in release_blog:
        calendar.append(shoes.text)
    return calendar
