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


EARLY_LINK = "https://www.capsuletoronto.com/products/"
CHECK_OUT_LINK = "https://www.capsuletoronto.com/cart/"
SHOP_PAY_LOG_IN = "https://shop.app/pay/authentication/login"
NEW_ARRIVAL_LINK = "https://www.capsuletoronto.com/collections/new-arrivals"


def capsule_toronto_fast_mode(driver, keywords, size):
    driver.get(NEW_ARRIVAL_LINK)
    boo = True
    # monitor + auto check out starts
    while boo:
        try:
            start1 = time.time()
            driver.find_element_by_css_selector(
                "a[href*='"+str(keywords)+"']").click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//label[@for="swatch-0-' + str(size) + '"]'))).click()
            driver.get(CHECK_OUT_LINK +
                       str(driver.current_url.split("variant=", 1)[1]+":1"))
            print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
            boo = False
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
        except:
            driver.refresh()
    time.sleep(600)
    driver.quit()


def capsule_toronto_safe_mode(driver, keywords, size):
    driver.get(NEW_ARRIVAL_LINK)
    boo = True
    while boo:
        try:
            start1 = time.time()
            driver.find_element_by_css_selector(
                "a[href*='"+str(keywords)+"']").click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//label[@for="swatch-0-' + str(size) + '"]'))).click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Add to cart']"))).click()
            # Covid Agreement
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.ID, "agree"))).click()
            WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
            print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
            boo = False
        except:
            driver.refresh()
    time.sleep(600)
    driver.quit()


def capsule_toronto_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE):
    keywords = str(KEYWORDS)
    size = str(SIZE)
    size = size.replace(".", "-") if "." in size else size
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
        capsule_toronto_safe_mode(driver, keywords, size)
    else:
        capsule_toronto_fast_mode(driver, keywords, size)
