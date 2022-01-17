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
LOG_IN = "https://nomadshop.net/account/"
NEW_ARRIVAL_LINK = "https://nomadshop.net/collections/new-arrivals"
CHECK_OUT_LINK = "https://nomadshop.net/cart/"


def nomad_main(PATH,EMAIL,PASSWORD):
    keyword = str(input("\nenter search keywords:\n")).lower()
    size = str(input("\nenter size:\n"))
    print("\nrunning...")
    driver = webdriver.Chrome(PATH)
    driver.get(LOG_IN)
    driver.find_element_by_id("customer_email").send_keys(EMAIL)
    driver.find_element_by_id("customer_password").send_keys(PASSWORD)
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
                "a[href*='"+str(keyword)+"']").click()
            WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
                (By.XPATH, '//*[contains(@id,'+str(size)+')]'))).click()
            driver.get(CHECK_OUT_LINK +
                       str(driver.current_url.split("variant=", 1)[1]+":1"))
            boo = False
        except:
            driver.refresh()
    time.sleep(600)