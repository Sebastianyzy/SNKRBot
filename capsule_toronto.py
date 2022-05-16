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

SHOP_PAY_LOG_IN = "https://shop.app/pay/authentication/login"
NEW_ARRIVAL_LINK = "https://www.capsuletoronto.com/collections/new-arrivals"


def shop_pay(driver):
    try:
        if WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Pay now']"))):
            while driver.find_element_by_xpath("//span[normalize-space()='Pay now']"):
                driver.find_element_by_xpath("//span[normalize-space()='Pay now']").click()
    except:  
        time.sleep(600)  

def capsule_toronto_safe_mode(driver, keywords, size):
    driver.get(NEW_ARRIVAL_LINK)
    boo = True
    while boo:
        try:
            start = time.time()
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
            print("carted: \n"+"--- %f seconds ---" % (time.time() - start))
            boo = False
            shop_pay(driver)
        except:
            driver.get(NEW_ARRIVAL_LINK)
    time.sleep(600)
    driver.quit()


def capsule_toronto_main(PATH, PROFILE_PATH, KEYWORDS, SIZE):
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
    capsule_toronto_safe_mode(driver, keywords, size)
