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
SHOP_PAY_LOG_IN = "https://shop.app/pay/authentication/login"
UPCOMING_RELEASES = "https://www.deadstock.ca/blogs/coming-soon"


def deadstock_generate_early_link(early_link, title):
    title = re.sub('[^0-9a-zA-Z]+', " ", title)
    array = title.split()
    ans = ""
    for c in array:
        ans += c.lower() + "-"
    return early_link + ans[:-1]


def deadstock_early_link_mode(driver, link_to_run, size):
    driver.get(link_to_run)
    boo = True
    # monitor + auto check out starts
    while boo:
        try:
            start1 = time.time()
            click_size = driver.find_element_by_id(
                "ProductSelect-option-Size-"+str(size))
            ActionChains(driver).move_to_element(
                click_size).click(click_size).perform()
            driver.get(CHECK_OUT_LINK +
                       str(driver.current_url.split("variant=", 1)[1]+":1"))
            boo = False
            print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
            start2 = time.time()
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Pay now']"))).click()
        except:
            driver.get(link_to_run)
    print("checked out: \n"+"--- %f seconds ---" % (time.time() - start2))
    time.sleep(600)
    driver.quit()


def deadstock_safe_mode(driver, keywords, size):
    driver.get(UPCOMING_RELEASES)
    boo = True
    # monitor + auto check out starts
    while boo:
        try:
            start1 = time.time()
            driver.find_element_by_css_selector(
                "a[href*='"+str(keywords)+"']").click()
            click_size = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
                (By.ID, "ProductSelect-option-Size-"+str(size))))
            ActionChains(driver).move_to_element(
                click_size).click(click_size).perform()
            driver.get(CHECK_OUT_LINK +
                       str(driver.current_url.split("variant=", 1)[1]+":1"))
            boo = False
            print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
            start2 = time.time()
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Pay now']"))).click()
        except:
            driver.get(UPCOMING_RELEASES)
    print("checked out: \n"+"--- %f seconds ---" % (time.time() - start2))
    time.sleep(600)
    driver.quit()


def deadstock_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE):
    keywords = str(KEYWORDS)
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
    if SAFE_MODE:
        deadstock_safe_mode(driver, keywords, size)
    else:
        link_to_run = deadstock_generate_early_link(EARLY_LINK, keywords)
        deadstock_early_link_mode(driver, link_to_run, size)
