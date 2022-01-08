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

UPCOMING_RELEASES = "https://www.deadstock.ca/blogs/coming-soon"
EARLY_LINK = "https://www.deadstock.ca/products/"
RELEASE_TITLE = "blog_release_title"
LOG_IN = "https://www.deadstock.ca/account/"
CHECK_OUT_LINK = "https://www.deadstock.ca/cart/"


def deadstock_generate_early_link(early_link, shoe_name):
    shoe_name = re.sub('[^0-9a-zA-Z]+', " ", shoe_name)
    array = shoe_name.split()
    i = 0
    ans = ""
    for c in array:
        ans += c.lower() + "-"
    return early_link+ans[:-1]


def deadstock_main(PATH):
    EMAIL = str(input("enter email:\n"))
    PASSWORD = str(getpass.getpass("enter password:\n"))
    title = str(input("enter title:\n"))
    size = str(input("enter size:\n"))
    link_to_run = deadstock_generate_early_link(EARLY_LINK, title)
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
    request = requests.get(link_to_run)
    bs = bs4.BeautifulSoup(request.text, "html.parser")
    scripts = bs.find_all("script")
    i = 100
    boo = True
    # monitor + auto check out starts
    while boo:
        for s in scripts:
            try:
                if("var meta" in s.text):
                    script = s.text
                    script = script.split('var meta = ')[1]
                    script = script.split(';\nfor (var attr in meta)')[0]
                    jsonStr = script
                    jsonObj = json.loads(jsonStr)
                    i = 0
                    length = len(jsonObj['product']['variants'])
                    while(i < length):
                        if jsonObj['product']['variants'][i]['public_title'][-len(size):] == size:
                            driver.get(
                                CHECK_OUT_LINK + str(jsonObj['product']['variants'][i]['id'])+":1")
                        i += 1
                    boo = False
            except:
                driver.refresh()
    time.sleep(600)

# while boo:
#     try:
#         driver.find_element_by_css_selector(
#             "a[href*='"+str(keywords)+"']").click()
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#             (By.XPATH, '//label[@for="swatch-0-' + str(size) + '"]'))).click()
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#             (By.ID, "AddToCartText-product-template"))).click()
#         # Covid Agreement
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#             (By.ID, "agree"))).click()
#         WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.NAME, "checkout"))).click()
#         boo = False
#     except:
#         driver.refresh()
# time.sleep(600)


# def deadstock_pull_calendar(driver, link, calendar):
#     driver.get(link)
#     release_blog = driver.find_elements_by_class_name(RELEASE_TITLE)
#     for shoes in release_blog:
#         calendar.append(shoes.text)
#     return calendar
