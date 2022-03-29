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

NEW_ARRIVAL_LINK = "https://nomadshop.net/collections/new-arrivals"
CHECK_OUT_LINK = "https://nomadshop.net/cart/"
SHOP_PAY_LOG_IN = "https://shop.app/pay/authentication/login"


def nomad_fast_mode(driver, keywords, size):
    driver.get(NEW_ARRIVAL_LINK)
    boo = True
    # monitor + auto check out starts
    while boo:
        try:
            start1 = time.time()
            driver.find_element_by_css_selector(
                "a[href*='"+str(keywords)+"']").click()
            WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
                (By.XPATH, '//*[contains(@id,'+str(size)+')]'))).click()
            driver.get(CHECK_OUT_LINK +
                       str(driver.current_url.split("variant=", 1)[1]+":1"))
            boo = False
            print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
            start2 = time.time()
            # PAY
            pay_now = WebDriverWait(driver, 60).until(EC.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space()='Pay now']")))
            ActionChains(driver).move_to_element(
                pay_now).click(pay_now).perform()
        except:
            driver.get(NEW_ARRIVAL_LINK)
    print("checked out: \n"+"--- %f seconds ---" % (time.time() - start2))
    time.sleep(600)
    driver.quit()


def nomad_safe_mode(driver, keywords, size):
    driver.get(NEW_ARRIVAL_LINK)
    boo = True
    # monitor + auto check out starts
    while boo:
        try:
            start1 = time.time()
            driver.find_element_by_css_selector(
                "a[href*='"+str(keywords)+"']").click()
            WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
                (By.XPATH, '//*[contains(@id,'+str(size)+')]'))).click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, "//span[normalize-space()='Add to Bag']"))).click()
            click_cart = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='1']")))   
            if click_cart:
                ActionChains(driver).move_to_element(
                    click_cart).click(click_cart).perform()
                boo = False     
                print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
            start2 = time.time()
            WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
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
        except:
            driver.get(NEW_ARRIVAL_LINK)
    #print("checked out: \n"+"--- %f seconds ---" % (time.time() - start2))
    time.sleep(600)
    driver.quit()


def nomad_main(PATH, PROFILE_PATH, KEYWORDS, SIZE, SAFE_MODE):
    keywords = str(KEYWORDS).lower()
    size = str(SIZE)
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
        nomad_safe_mode(driver, keywords, size)
    else:
        nomad_fast_mode(driver, keywords, size)

