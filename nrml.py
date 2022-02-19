from cgi import test
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

EARLY_LINK = "https://nrml.ca/products/"
LOG_IN = "https://nrml.ca/account"
SHOP_PAY_LOG_IN = "https://shop.app/pay/authentication/login"


def nrml_generate_early_link(early_link, title):
    title = re.sub('[^0-9a-zA-Z]+', " ", title)
    array = title.split()
    ans = ""
    for c in array:
        ans += c.lower() + "-"
    return early_link+ans[:-1]


def nrml_main(PATH,EMAIL,PASSWORD):
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
            start = time.time()
            driver.find_element_by_id("Option1-"+str(size)).click()
            driver.find_element_by_class_name("add-to-cart").click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
            boo = False
        except:
            driver.refresh()
    print("--- %f seconds ---" % (time.time() - start))        
    time.sleep(600)


def nrml_link_to_run(keyword, driver):
    driver.find_element_by_id("search").send_keys(keyword)
    driver.find_element_by_xpath("//button[@type='submit']")


def dunk_script(PATH, PROFILE_PATH):
    size = str(10)
    link_to_run = "https://nrml.ca/pages/search-results?q=DD1391%20701"
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
    driver.get(link_to_run)
    boo = True
    # monitor + auto check out starts
    while boo:
        try:
            start1 = time.time()
            ActionChains(driver).move_to_element(driver.find_element_by_tag_name("h3")).perform()
            click_size = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='"+size+"']")))
            ActionChains(driver).move_to_element(click_size).click(click_size).perform()
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
            boo = False
            print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
            start2 = time.time()
            WebDriverWait(driver, 120).until(EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Pay now']"))).click()
        except:
            driver.refresh()
    print("checked out: \n"+"--- %f seconds ---" % (time.time() - start2))
    time.sleep(600)

# dunk_script("/Users/seb/Chromedriver/chromedriver","/Users/seb/Library/Application Support/Google/Chrome/Default")



def yeezy_script_fastmode(PATH, PROFILE_PATH):
    title = "YEEZY 500 DB2908"
    size = str(12)
    link_to_run = nrml_generate_early_link(EARLY_LINK, title)
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
    driver.get(link_to_run)
    boo = True
    while boo:
        try:
            start1 = time.time()
            driver.find_element_by_id("Option1-"+str(size)).click()
            driver.find_element_by_class_name("add-to-cart").click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
            boo = False
            print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
            start2 = time.time()
            WebDriverWait(driver, 120).until(EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Pay now']"))).click()
        except:
            driver.refresh()
    print("--- %f seconds ---" % (time.time() - start2))        
    time.sleep(600)
