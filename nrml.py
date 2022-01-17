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





# def test(PATH):
#     size = 8.5
#     driver = webdriver.Chrome(PATH)
#     driver.get("https://nrml.ca/products/wmns-air-jordan-5-retro-dd9336-400")
#     boo = True
#     while boo:
#         try:
#             start = time.time()
#             driver.find_element_by_id("Option1-"+str(size)).click()
#             driver.find_element_by_class_name("add-to-cart").click()
#             WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#                 (By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
#             boo = False
#         except:
#             driver.refresh()  
#     timecost = ("--- %f seconds ---" % (time.time() - start))
#     array.append(str(timecost))
#     time.sleep(10)              
#     driver.quit()   


# i = 0
# array = []
# while(i<=2):
#     test("/Users/seb/Chromedriver/chromedriver")
#     i+=1

# for t in array:
#     print(t)
