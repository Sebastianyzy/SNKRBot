import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

UPCOMING_RELEASES = "https://www.capsuletoronto.com/pages/launches"
EARLY_LINK = "https://www.capsuletoronto.com/products/"
LOG_IN = "https://www.capsuletoronto.com/account"
RELEASE_TITLE = "address"


def run_capsule_toronto(driver, PATH):
    LOG_IN = "https://www.capsuletoronto.com/account"
    new_arrival_link = "https://www.capsuletoronto.com/collections/new-arrivals" #"https://www.capsuletoronto.com/collections/new-arrivals/footwear" #"https://www.capsuletoronto.com/products/air-jordan-11-low-ie-919712-023-black"#"https://nrml.ca/products/air-jordan-1-retro-high-og-555088-063" #"https://nrml.ca/products/w-nike-dunk-low-se-dd7099-001"
    EMAIL = "sebyzy@gmail.com"
    PASSWORD =
    driver = webdriver.Chrome(PATH)
    driver.get(LOG_IN)
    driver.find_element_by_id("CustomerEmail").send_keys(EMAIL)
    driver.find_element_by_id("CustomerPassword").send_keys(PASSWORD)
    driver.find_element_by_xpath("//input[@type='submit']").click()
    time.sleep(60)
    driver.refresh()
    driver.maximize_window()
    driver.get(new_arrival_link)
    boo = True
    while boo:
        try:
            driver.find_element_by_css_selector("a[href*='air-jordan-11-retro-ct8012-005']").click()
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//label[@for="swatch-0-12"]'))).click()
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "AddToCartText-product-template"))).click()
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "agree"))).click() #Covid Agreement   
            #WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, "checkout"))).click()
            boo = False
        except:
            driver.refresh()
    time.sleep(180)


def capsule_bot_configure(calendar, shoes):
    color = input("enter color:\n")
    return capsule_generate_early_link(calendar[shoes-1], EARLY_LINK, str(color))  


def capsule_generate_early_link(s, site, color):
    link = ""
    s.lstrip()
    s.rstrip()
    for char in s: 
        if(char == " " or char == "-"):
            link += "-"
        elif(char.isalpha() or char. isnumeric()):
            link += char.lower() 
    return site+link+color


def capsule_toronto_pull_calendar(driver, link, calendar):   
    driver.get(link)
    release_blog = driver.find_elements_by_class_name(RELEASE_TITLE)
    for shoes in release_blog:
        calendar.append(shoes.text)
    return calendar
