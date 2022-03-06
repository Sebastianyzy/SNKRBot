import selenium
import time
import getpass
import re
import bs4
import requests
import json
import harvester
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


EARLY_LINK = "https://size.ca/products/"
NEW_ARRIVAL_LINK = "https://size.ca/collections/new-in"
LOG_IN = "https://size.ca/account/"
SHOP_PAY_LOG_IN = "https://shop.app/pay/authentication/login"
CHECK_OUT_LINK = "https://size.ca/cart/"


def size_ca_generate_early_link(early_link, title):
    title = re.sub("'", "", title)
    title = re.sub("’", "", title)
    title = re.sub("‘", "", title)
    title = re.sub('[^0-9a-zA-Z]+', " ", title)
    array = title.split()
    ans = ""
    for c in array:
        ans += c.lower() + "-"
    return early_link+ans[:-1]


def size_ca_early_link_mode(driver, link_to_run, size):
    boo = True
    driver.get(link_to_run)
    while boo:
        try:
            start1 = time.time()
            driver.find_element_by_id("shopify-section-product-template")
            click_size = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//label[normalize-space()='"+str(size)+"']")))
            ActionChains(driver).move_to_element(click_size).click(click_size).perform()
            add_to_cart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Add to Bag']")))
            ActionChains(driver).move_to_element(add_to_cart).click(add_to_cart).perform()
            boo = False
            print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
            start2 = time.time()
            shop_pay = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='ShopPay']")))
            ActionChains(driver).move_to_element(shop_pay).click(shop_pay).perform()
            # PAY
            # pay_now = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Pay now']")))
            # ActionChains(driver).move_to_element(
            #     pay_now).click(pay_now).perform()
        except:
            driver.get(link_to_run)
    print("checked out: \n"+"--- %f seconds ---" % (time.time() - start2))
    time.sleep(600)
    driver.quit()

    # while boo:
    #     try:
    #         start1 = time.time()
    #         driver.find_element_by_xpath(
    #             "//label[normalize-space()='"+str(size)+"']").click()
    #         driver.get(CHECK_OUT_LINK +
    #                    str(driver.current_url.split("variant=", 1)[1]+":1"))
    #         print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
    #         boo = False
    #         start2 = time.time()
    #         # # PAY
    #         #BUG
    #         # WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
    #         #     (By.XPATH, "//span[normalize-space()='Pay now']"))).click()
    #     except:
    #         driver.get(link_to_run)
    # print("checked out: \n"+"--- %f seconds ---" % (time.time() - start2))
    # time.sleep(600)
    # driver.quit()


def size_ca_safe_mode(driver, keywords, size):
    driver.get(NEW_ARRIVAL_LINK)
    boo = True
    # monitor + auto check out starts
    while boo:
        try:
            start1 = time.time()
            driver.find_element_by_css_selector(
                "a[href*='"+str(keywords)+"']").click()
            click_size = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//label[normalize-space()='"+str(size)+"']")))
            ActionChains(driver).move_to_element(click_size).click(click_size).perform()
            add_to_cart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Add to Bag']")))
            ActionChains(driver).move_to_element(add_to_cart).click(add_to_cart).perform()
            boo = False
            print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
            start2 = time.time()
            shop_pay = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='ShopPay']")))
            ActionChains(driver).move_to_element(shop_pay).click(shop_pay).perform()
            # PAY
            pay_now = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Pay now']")))
            ActionChains(driver).move_to_element(
                pay_now).click(pay_now).perform()
        except:
            driver.get(NEW_ARRIVAL_LINK)
    print("checked out: \n"+"--- %f seconds ---" % (time.time() - start2))
    time.sleep(600)
    driver.quit()


def size_ca_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE):
    keywords = str(KEYWORDS)
    size = str(SIZE)
    link_to_run = size_ca_generate_early_link(EARLY_LINK, keywords) 
    print("\nrunning...")
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir='+PROFILE_PATH)
    options.add_argument('--profile-directory='+PROFILE_PATH)
    driver = webdriver.Chrome(options=options, executable_path=PATH)
    driver.get(SHOP_PAY_LOG_IN)
    time.sleep(60)
    # idle 60s
    driver.refresh()
    driver.maximize_window()
    if SAFE_MODE:
        size_ca_safe_mode(driver, keywords, size)
    else:
        size_ca_early_link_mode(driver, link_to_run, size)

