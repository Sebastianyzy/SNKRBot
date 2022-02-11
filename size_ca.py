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


EARLY_LINK = "https://size.ca/products/"
NEW_ARRIVAL_LINK = "https://size.ca/collections/new-in"
LOG_IN = "https://size.ca/account/"
SHOP_PAY_LOG_IN = "https://shop.app/pay/authentication/login"
CHECK_OUT_LINK = "https://size.ca/cart/"


def size_ca_generate_early_link(early_link, title):
    title = re.sub("'", "", title)
    title = re.sub('[^0-9a-zA-Z]+', " ", title)
    array = title.split()
    ans = ""
    for c in array:
        ans += c.lower() + "-"
    return early_link+ans[:-1]


def size_ca_main(PATH, EMAIL, PASSWORD):
    title = str(input("\nenter title:\n"))
    size = str(input("\nenter size:\n"))
    link_to_run = size_ca_generate_early_link(EARLY_LINK, title)
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
    while boo:
        try:
            driver.find_element_by_xpath(
                "//label[normalize-space()='"+str(size)+"']").click()
            driver.get(CHECK_OUT_LINK +
                       str(driver.current_url.split("variant=", 1)[1]+":1"))
            boo = False
        except:
            driver.refresh()
    time.sleep(600)

    # # auto checkout method
    # while boo:
    # try:
    #     driver.find_element_by_xpath("//label[normalize-space()='"+str(size)+"']").click()
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "AddToCartText"))).click()
    #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Checkout securely']"))).click()
    #     boo = False
    # except:
    #     driver.refresh()


# def new_balance_script(PATH, PROFILE_PATH):
#     keywords = "bb550hl1"
#     size = "10.5"
#     print("\nrunning...")
#     options = webdriver.ChromeOptions()
#     options.add_argument('--user-data-dir='+PROFILE_PATH)
#     options.add_argument('--profile-directory='+PROFILE_PATH)
#     driver = webdriver.Chrome(options=options, executable_path=PATH)
#     driver.get(SHOP_PAY_LOG_IN)
#     # idle 120s
#     time.sleep(60)
#     driver.refresh()
#     driver.maximize_window()
#     driver.get(NEW_ARRIVAL_LINK)
#     boo = True
#     # monitor + auto check out starts
#     while boo:
#         try:
#             start1 = time.time()
#             driver.find_element_by_css_selector(
#                 "a[href*='"+str(keywords)+"']").click()
#             WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//label[normalize-space()='"+str(size)+"']"))).click()    
#             # driver.get(CHECK_OUT_LINK + str(driver.current_url.split("variant=", 1)[1]+":1"))
#             # driver.find_element_by_xpath("//label[normalize-space()='"+str(size)+"']").click()
#             WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "AddToCartText"))).click()
#             WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='ShopPay']"))).click()
#             boo = False
#             print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
#             start2 = time.time()
#             boo = False
#             # PAY
#             WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Pay now']"))).click()
#         except:
#             driver.refresh()
#     print("checked out: \n"+"--- %f seconds ---" % (time.time() - start2))
#     time.sleep(600)

