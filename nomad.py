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
SHOP_PAY_LOG_IN = "https://shop.app/pay/authentication/login"


def nomad_main(PATH, PROFILE_PATH, KEYWORDS, SIZE):
    keyword = str(KEYWORDS).lower()
    size = str(SIZE)
    print("\nrunning...")
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir='+PROFILE_PATH)
    options.add_argument('--profile-directory='+PROFILE_PATH)
    driver = webdriver.Chrome(options=options, executable_path=PATH)
    driver.get(SHOP_PAY_LOG_IN)
    # idle 60s
    time.sleep(60)
    driver.refresh()
    driver.maximize_window()
    driver.get(NEW_ARRIVAL_LINK)
    boo = True
    # monitor + auto check out starts
    while boo:
        try:
            start1 = time.time()
            driver.find_element_by_css_selector(
                "a[href*='"+str(keyword)+"']").click()
            WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
                (By.XPATH, '//*[contains(@id,'+str(size)+')]'))).click()
            driver.get(CHECK_OUT_LINK +
                       str(driver.current_url.split("variant=", 1)[1]+":1"))
            boo = False
            print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
            start2 = time.time()
            WebDriverWait(driver, 120).until(EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Pay now']"))).click()
        except:
            driver.refresh()
    print("checked out: \n"+"--- %f seconds ---" % (time.time() - start2))
    time.sleep(600)  