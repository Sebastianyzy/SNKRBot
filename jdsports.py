import selenium
import time
import re
from kernal import SHOP_PAY_LOG_IN
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


EARLY_LINK = "https://jdsports.ca/products/"
SEARCH_LINK = "https://jdsports.ca/search?q="

def shop_pay_check_out(driver):
    try:
        if WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Pay now']"))):
            while driver.find_element_by_xpath("//span[normalize-space()='Pay now']"):
                driver.find_element_by_xpath("//span[normalize-space()='Pay now']").click()
    except:  
        time.sleep(600)  

def jd_generate_early_link(early_link, title):
    title = re.sub('[^0-9a-zA-Z]+', " ", title)
    array = title.split()
    ans = ""
    for c in array:
        ans += c.lower() + "-"
    return early_link+ans[:-1]


def jd_generate_search_link(search_link, title):
    return search_link+title


def jd_safe_mode(driver, size, link_to_run, keywords):
    driver.get(link_to_run)
    boo = True
    while boo:
        try:
            start1 = time.time()
            find_product = driver.find_element_by_css_selector(
                "a[href*='"+str(keywords)+"']")
            driver.get(find_product.get_attribute("href"))
            click_size = driver.find_element_by_xpath(
                "//label[normalize-space()='"+str(size)+"']")
            ActionChains(driver).move_to_element(
                click_size).click(click_size).perform()
            add_to_cart = driver.find_element_by_xpath(
                "//button[normalize-space()='ADD TO BASKET']")
            ActionChains(driver).move_to_element(
                add_to_cart).click(add_to_cart).perform()
            shop_pay = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@class='btn btn--secondary'][normalize-space()='PAYMENT OPTIONS']")))
            ActionChains(driver).move_to_element(
                shop_pay).click(shop_pay).perform()
            WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
            boo = False
            print("\n"+"carted: \n"+"--- %f seconds ---" %
                  (time.time() - start1)+"\n"+"checking out...\n")
            shop_pay_check_out(driver)
        except:
            driver.get(link_to_run)
    time.sleep(600)
    driver.quit()


def jd_fast_mode(driver, size, link_to_run):
    driver.get(link_to_run)
    boo = True
    while boo:
        try:
            start1 = time.time()
            click_size = driver.find_element_by_xpath(
                "//label[normalize-space()='"+str(size)+"']")
            ActionChains(driver).move_to_element(
                click_size).click(click_size).perform()
            add_to_cart = driver.find_element_by_xpath(
                "//button[normalize-space()='ADD TO BASKET']")
            ActionChains(driver).move_to_element(
                add_to_cart).click(add_to_cart).perform()
            shop_pay = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@class='btn btn--secondary'][normalize-space()='PAYMENT OPTIONS']")))
            ActionChains(driver).move_to_element(
                shop_pay).click(shop_pay).perform()
            WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
            boo = False
            print("\n"+"carted: \n"+"--- %f seconds ---" %
                  (time.time() - start1)+"\n"+"checking out...\n")
            shop_pay_check_out(driver)
        except:
            driver.get(link_to_run)
    time.sleep(600)
    driver.quit()


def jd_sports_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE, SAFE_MODE_STYLE_CODE):
    print("\nrunning...")
    link_to_run = jd_generate_search_link(
        SEARCH_LINK, SAFE_MODE_STYLE_CODE) if SAFE_MODE else jd_generate_early_link(EARLY_LINK, KEYWORDS)
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
        jd_safe_mode(driver, SIZE, link_to_run, KEYWORDS)
    else:
        jd_fast_mode(driver, SIZE, link_to_run)
