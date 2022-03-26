import selenium
import time
import getpass
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
LOG_IN = "https://www.capsuletoronto.com/account"
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
            start2 = time.time()
            boo = False
            # PAY
            # Bug
            # WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
            #     (By.XPATH, "//span[normalize-space()='Pay now']"))).click()
        except:
            driver.refresh()
    print("checked out: \n"+"--- %f seconds ---" % (time.time() - start2))
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
            start2 = time.time()
            boo = False
            ########Test pay_button
            ##########################################################################################
            if WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Pay now']"))):
                WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Pay now']"))).click()
                print("\n"+"checking out...\n")
                print("in checkout line...: \n"+"--- %f seconds ---" % (time.time() - start2))

   
                

            print("solving capcha")
            start4 = time.time()
            result = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='visually-hidden']")))
            print("retuslt:\n"+result.text+"\n")
            print("result_bynames\n"+driver.find_elements_by_xpath("//h1[@class='visually-hidden']").text+"\n")
            print("result: \n"+"--- %f seconds ---" % (time.time() - start4))    

            # ActionChains(driver).move_to_element(
            #     pay_now).click(pay_now).perform()
            ###############################################################################################
        except:
            driver.refresh()
    #print("checked out: \n"+"--- %f seconds ---" % (time.time() - start2))
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


PATH = "/Users/seb/Chromedriver/chromedriver"
PROFILE_PATH = "/Users/seb/Library/Application Support/Google/Chrome/Default"
KEYWORDS = "air-max-1"
SIZE = "10"
SAFE_MODE = True

capsule_toronto_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE)

