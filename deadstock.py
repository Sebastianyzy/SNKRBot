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


EARLY_LINK = "https://www.deadstock.ca/products/"
LOG_IN = "https://www.deadstock.ca/account/"
CHECK_OUT_LINK = "https://www.deadstock.ca/cart/"


def deadstock_generate_early_link(early_link, title):
    title = re.sub('[^0-9a-zA-Z]+', " ", title)
    array = title.split()
    ans = ""
    for c in array:
        ans += c.lower() + "-"
    return early_link+ans[:-1]


def deadstock_main(PATH,EMAIL,PASSWORD):
    title = str(input("\nenter title:\n"))
    size = str(input("\nenter size:\n"))
    link_to_run = deadstock_generate_early_link(EARLY_LINK, title)
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
    driver.get(link_to_run)
    boo = True
    # monitor + auto check out starts
    while boo:
        try:
            click_size = driver.find_element_by_id("ProductSelect-option-Size-"+str(size)) 
            ActionChains(driver).move_to_element(click_size).click(click_size).perform()
            driver.get(CHECK_OUT_LINK + str(driver.current_url.split("variant=",1)[1]+":1"))
            boo = False
        except:
            driver.refresh()
    time.sleep(600)
