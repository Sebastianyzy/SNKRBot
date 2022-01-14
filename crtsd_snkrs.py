from asyncio import sleep
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

UPCOMING_RELEASES = "https://www.courtsidesneakers.com/pages/upcoming-releases"
EARLY_LINK = "https://www.courtsidesneakers.com/products/"
LOG_IN = "https://www.courtsidesneakers.com/account"



def crtsd_snkrs__generate_early_link(early_link, title):
    title = re.sub("'", "", title)
    title = re.sub('[^0-9a-zA-Z]+', " ", title)
    array = title.split()
    ans = ""
    for c in array:
        ans += c.lower() + "-"
    return early_link+ans[:-1]

def crtsd_snkrs_main(PATH):
    EMAIL = "sebyzy@gmail.com"#str(input("enter email:\n"))
    PASSWORD = "hrLyWaXp5MKiH!S"#str(getpass.getpass("\nenter password:\n"))
    title = "New Balance BB550HL1"#str(input("\nenter title:\n"))
    size = 10#str(input("\nenter size:\n"))
    link_to_run = crtsd_snkrs__generate_early_link(EARLY_LINK, title)
    print("\nrunning...")
    driver = webdriver.Chrome(PATH)
    driver.get(LOG_IN)
    driver.find_element_by_id("CustomerEmail").send_keys(EMAIL)
    driver.find_element_by_id("CustomerPassword").send_keys(PASSWORD)
    driver.find_element_by_xpath("//button[normalize-space()='Sign In']").click()
    time.sleep(60)
    driver.refresh()
    driver.get(link_to_run)
    boo = True
    while boo:
        try:
            driver.find_element_by_xpath("//label[normalize-space()='"+str(size)+"']").click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Add to cart']"))).click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
            boo = False
        except:
            driver.refresh()
    time.sleep(600)


def new_balance_script(PATH):
    EMAIL = "sebyzy@gmail.com"
    PASSWORD = "hrLyWaXp5MKiH!S"
    title = "New Balance M1500BSG"#"New Balance BB550HL1"
    size = 10
    link_to_run = crtsd_snkrs__generate_early_link(EARLY_LINK, title)
    print("\nrunning...")
    driver = webdriver.Chrome(PATH)
    driver.get(LOG_IN)
    driver.find_element_by_id("CustomerEmail").send_keys(EMAIL)
    driver.find_element_by_id("CustomerPassword").send_keys(PASSWORD)
    driver.find_element_by_xpath("//button[normalize-space()='Sign In']").click()
    time.sleep(120)
    driver.refresh()
    driver.get(link_to_run)
    boo = True
    while boo:
        try:
            driver.find_element_by_xpath("//label[normalize-space()='"+str(size)+"']").click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Add to cart']"))).click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))).click()
            boo = False
        except:
            driver.refresh()
    time.sleep(600)

#new_balance_script("/Users/seb/Chromedriver/chromedriver")