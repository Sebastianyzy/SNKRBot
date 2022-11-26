import selenium
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

EARLY_LINK = "https://nrml.ca/products/"
SHOP_PAY_LOG_IN = "https://shop.app/pay/authentication/login"
SEARCH_LINK = "https://nrml.ca/search?q="


def shop_pay_check_out(driver):
    try:
        if WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Pay now']"))):
            while driver.find_element_by_xpath("//span[normalize-space()='Pay now']"):
                driver.find_element_by_xpath(
                    "//span[normalize-space()='Pay now']").click()
    except:
        time.sleep(600)


def nrml_generate_early_link(early_link, title):
    title = re.sub('[^0-9a-zA-Z]+', " ", title)
    array = title.split()
    ans = ""
    for c in array:
        ans += c.lower() + "-"
    return early_link+ans[:-1]


def nrml_generate_search_link(search_link, title):
    return search_link+title


def nrml_safe_mode(driver, size, link_to_run, keywords):
    driver.get(link_to_run)
    boo = True
    # monitor + auto check out starts
    while boo:
        try:
            start1 = time.time()
            find_product = driver.find_element_by_css_selector(
                "a[href*='"+str(keywords)+"']:not([href*='/blogs/'])")
            driver.get(find_product.get_attribute("href"))
            driver.find_element_by_xpath("//label[normalize-space()='"+str(size)+"']").click()
            try:
                driver.find_element_by_css_selector("div[data-testid='ShopifyPay-button'][role='button']").click()
            except:
                driver.find_element_by_class_name("add-to-cart").click()               
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
            boo = False
            print("\n"+"carted: \n"+"--- %f seconds ---" %
                  (time.time() - start1)+"\n"+"checking out...\n")
            shop_pay_check_out(driver)
        except:
            try:
                driver.get(link_to_run)
            except:
                try:
                    driver.refresh()
                    driver.get(link_to_run)
                except:
                    driver.get("https://nrml.ca/")
                    driver.refresh()
                    driver.get(link_to_run)
    time.sleep(600)
    driver.quit()


def nrml_fast_mode(driver, size, link_to_run):
    driver.get(link_to_run)
    boo = True
    while boo:
        try:
            start1 = time.time()
            driver.find_element_by_xpath("//label[normalize-space()='"+str(size)+"']").click()
            try:
                driver.find_element_by_css_selector("div[data-testid='ShopifyPay-button'][role='button']").click()
            except:
                driver.find_element_by_class_name("add-to-cart").click()               
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
            boo = False
            print("\n"+"carted: \n"+"--- %f seconds ---" %
                  (time.time() - start1)+"\n"+"checking out...\n")
            shop_pay_check_out(driver)
        except:
            driver.get(link_to_run)
    time.sleep(600)
    driver.quit()


def nrml_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE):
    keywords = str(KEYWORDS)
    size = str(SIZE)
    link_to_run = nrml_generate_search_link(
        SEARCH_LINK, keywords) if SAFE_MODE else nrml_generate_early_link(EARLY_LINK, keywords)
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
        nrml_safe_mode(driver, size, link_to_run, keywords.lower())
    else:
        nrml_fast_mode(driver, size, link_to_run)
