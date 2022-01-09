import selenium
import time
import getpass
import re
import bs4
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

UPCOMING_RELEASES = "https://nrml.ca/blogs/release-calendar"
EARLY_LINK = "https://nrml.ca/products/"
RELEASE_TITLE = "font-heading"
LOG_IN = "https://nrml.ca/account"


def nrml_main(PATH):
    EMAIL = str(input("enter email:\n"))
    PASSWORD = str(getpass.getpass("\nenter password:\n"))
    title = str(input("\nenter title:\n"))
    size = str(input("\nenter size:\n"))
    link_to_run = nrml_generate_early_link(EARLY_LINK, title)
    print("\nrunning...")
    driver = webdriver.Chrome(PATH)
    driver.get(LOG_IN)
    driver.find_element_by_id("CustomerEmail").send_keys(EMAIL)
    driver.find_element_by_id("CustomerPassword").send_keys(PASSWORD)
    driver.find_element_by_class_name("btn").click()
    time.sleep(60)
    driver.refresh()
    driver.get(link_to_run)
    boo = True
    while boo:
        try:
            driver.find_element_by_id("Option1-"+str(size)).click()
            driver.find_element_by_class_name("add-to-cart").click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
            boo = False
        except:
            driver.refresh()
    time.sleep(600)        


def nrml_generate_early_link(early_link, title):
    title = re.sub('[^0-9a-zA-Z]+', " ", title)
    array = title.split()
    ans = ""
    for c in array:
        ans += c.lower() + "-"
    return early_link+ans[:-1]


def nrml_pull_calendar(driver, link, calendar):
    driver.get(link)
    release_blog = driver.find_elements_by_class_name(RELEASE_TITLE)
    for shoes in release_blog:
        calendar.append(shoes.text)
    return calendar
