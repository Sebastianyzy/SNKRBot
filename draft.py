from argparse import Action
import imp
from selenium.webdriver.remote.webelement import WebElement
import capsule_toronto
import deadstock
import nrml
import size_ca
import crtsd_snkrs
import re
import nomad
import getpass
import selenium
import bs4
import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium_stealth import stealth
import harvester
from harvester import Harvester
# from harvester import ReCaptchaV2
# from harvester import ReCaptchaV3
# from harvester import hCaptcha
# from harvester import Proxy

# # #######################################################################################################################
# # #HAVEN
# PATH = "/Users/seb/Chromedriver/chromedriver"
# PROFILE_PATH = "/Users/seb/Library/Application Support/Google/Chrome/Default"
# def haven_kwondo1(PATH, PROFILE_PATH):
#     keywords = "kwondo"
#     size = "10"
#     print("\nrunning...")
#     options = webdriver.ChromeOptions()
#     options.add_argument('--user-data-dir='+PROFILE_PATH)
#     options.add_argument('--profile-directory='+PROFILE_PATH)
#     driver = webdriver.Chrome(options=options, executable_path=PATH)
#     driver.get("https://shop.app/pay/authentication/login")
#     # idle 60s
#     time.sleep(60)
#     driver.refresh()
#     driver.maximize_window()
#     driver.get("https://shop.havenshop.com/collections/new-arrivals")
#     boo = True
#     # monitor + auto check out starts
#     while boo:
#         try:
#             start1 = time.time()
#             driver.find_element_by_css_selector(
#                 "a[href*='"+str(keywords)+"']").click()
#             WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#                 (By.XPATH, '//label[@data-value="'+str(size)+'US"]'))).click()
#             click_size = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#                 (By.XPATH, '//button[normalize-space()="Add to bag"]')))
#             ActionChains(driver).move_to_element(
#                 click_size).click(click_size).perform()
#             WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
#                 (By.XPATH, '//span[@class="indicator"]')))
#             driver.find_element_by_css_selector(
#                 "a[href*='"+str("/cart")+"']").click()
#             print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
#             start2 = time.time()
#             boo = False
#             # PAY
#             #WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Pay now']"))).click()
#         except:
#             driver.get("https://shop.havenshop.com/collections/new-arrivals")
#     print("checked out: \n"+"--- %f seconds ---" % (time.time() - start2))
#     time.sleep(600)
# driver = webdriver.Chrome(PATH)
# driver.get(
#     "https://shop.havenshop.com/checkpoint?return_to=https%3A%2F%2Fshop.havenshop.com%2Fcart")
# driver.maximize_window()
# size = "9.5"
# #captcha = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='recaptcha-checkbox-border'][role='presentation']")))
# captcha = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#     (By.XPATH, "//span[normalize-space()='I'm not a robot']]")))
# ActionChains(driver).move_to_element(captcha).click(captcha).perform()
# # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//label[@data-value="'+str(size)+'US"]'))).click()
# # click_size = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[normalize-space()="Add to bag"]')))
# # ActionChains(driver).move_to_element(click_size).click(click_size).perform()
# # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//span[@class="indicator"]')))
# # driver.find_element_by_css_selector("a[href*='"+str("/cart")+"']").click()
# # click_checkout = WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, '//input[@type="submit"]'))).click()
# # ActionChains(driver).move_to_element(click_checkout).click(click_checkout).perform()
# time.sleep(5)
# driver.close()
# #######################################################################################################################





# #######################################################################################################################
# #BB BRANDED
# PATH = "/Users/seb/Chromedriver/chromedriver"
# PROFILE_PATH = "/Users/seb/Library/Application Support/Google/Chrome/Default"
# def jordan3_script(PATH, PROFILE_PATH):
#     keywords = "ct8532-126"
#     size = "11"
#     print("\nrunning...")
#     options = webdriver.ChromeOptions()
#     options.add_argument('--user-data-dir='+PROFILE_PATH)
#     options.add_argument('--profile-directory='+PROFILE_PATH)
#     driver = webdriver.Chrome(options=options, executable_path=PATH)
#     driver.get("https://shop.app/pay/authentication/login")
#     # idle 60s
#     time.sleep(60)
#     driver.refresh()
#     driver.maximize_window()
#     driver.get("https://www.bbbranded.com/collections/release-calendar")
#     boo = True
#     # monitor + auto check out starts
#     while boo:
#         try:
#             start1 = time.time()
#             driver.find_element_by_css_selector("a[href*='"+str(keywords)+"']").click()
#             WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//li[@data-text="'+str(size)+'"]'))).click()
#             driver.get("https://www.bbbranded.com/cart/" +str(driver.current_url.split("variant=", 1)[1]+":1"))
#             print("carted: \n"+"--- %f seconds ---" % (time.time() - start1))
#             start2 = time.time()
#             boo = False
#             #PAY
#             WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Pay now']"))).click()
#         except:
#             driver.get("https://www.bbbranded.com/collections/release-calendar")
#     print("checked out: \n"+"--- %f seconds ---" % (time.time() - start2))
#     time.sleep(600)

# actual link: https://www.bbbranded.com/collections/release-calendar/products/air-jordan-3-retro-ct8532-126

# jordan3_script(PATH,PROFILE_PATH)

# #######################################################################################################################


print("draft\n----------------------------\n\n\n\n")

# captcha = harvester.Harvester.intercept_recaptcha_v2(
#     url='www.supremenewyork.com',
#     sitekey='6LeWwRkUAAAAAOBsau7KpuC9AV-6J8mhw4AjC3Xz'
# )

# harvester = Harvester().serveforever()
# intercepter = harvester.capture(captcha)


PATH = "/Users/seb/Chromedriver/chromedriver"
PROFILE_PATH = "/Users/seb/Library/Application Support/Google/Chrome/Default"
driver = webdriver.Chrome(PATH)
driver.maximize_window()

size = 11.5
#driver.get("https://shop.havenshop.com/checkpoint?return_to=https%3A%2F%2Fshop.havenshop.com%2Fcart")
driver.get("https://www.sportchek.ca/categories/men/footwear/basketball-shoes/product/nike-mens-jordan-why-not-zero5-childhood-basketball-shoes-color-333542896_04-333542896.html#")
driver.maximize_window()
driver.find_element_by_xpath("//span[normalize-space()='"+str(size)+"']").click()
#driver.find_element_by_xpath("//span[normalize-space()='Add To Cart']").click()
add_to_cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add To Cart']"))).click()   


#add_to_cart.click_and_hold(on_element=click_size)

# web = "https://www.sportchek.ca/categories/men/footwear/basketball-shoes/product/nike-mens-jordan-why-not-zero5-childhood-basketball-shoes-color-333542896_04-333542896.html#333542896=333542912"
# wen2 = "https://www.sportchek.ca/categories/men/footwear/basketball-shoes/product/nike-mens-jordan-why-not-zero5-childhood-basketball-shoes-color-333542896_04-333542896.html#333542896=333542912"
                
# captcha = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='recaptcha-checkbox-border'][role='presentation']")))
# captcha = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='I'm not a robot']]")))
# ActionChains(driver).move_to_element(captcha).click(captcha).perform()

print("done")              
time.sleep(50)
driver.quit()
quit() 

       


    



# def process_browser_log_entry(entry):
#     response = json.loads(entry['message'])['message']
#     return response

# browser_log = driver.get_log('browser')
# print(browser_log)
# # events = [process_browser_log_entry(entry) for entry in browser_log]
# # events = [event for event in events if 'Network.response' in event['method']]

# driver.quit


# options = webdriver.ChromeOptions()
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--user-data-dir=/Users/seb/Library/Application Support/Google/Chrome/Default')
# options.add_argument('--profile-directory=/Users/seb/Library/Application Support/Google/Chrome/Default')
# driver = webdriver.Chrome(options=options, executable_path=PATH)
# stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )
# driver.get("https://stackoverflow.com/questions/69441729/python-selenium-use-chromedriver-again")


# time.sleep(60)

# options.add_argument("start-maximized")

# options.add_argument("--headless")

# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('--user-data-dir=/Users/seb/Library/Application Support/Google/Chrome/Default')
# options.add_argument('--profile-directory=/Users/seb/Library/Application Support/Google/Chrome/Default')
# driver = webdriver.Chrome(options=options, executable_path=PATH)

# stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )

# url = "https://bot.sannysoft.com/"
# driver.get(url)
# time.sleep(5)
# # #driver.quit()

# options = webdriver.ChromeOptions()
# options.add_argument('--user-data-dir=/Users/seb/Library/Application Support/Google/Chrome/Default')
# options.add_argument('--profile-directory=/Users/seb/Library/Application Support/Google/Chrome/Default')

# driver = webdriver.Chrome(executable_path=PATH, options=options)

# driver.get("https://www.deadstock.ca/account")


# # Import required packages, modules etc.. Selenium is a must!

# def login(username, password):       # Logs in the user
#     driver.get("https://stackoverflow.com/users/login")
#     WebDriverWait(driver, 60).until(EC.presence_of_element_located(
#         (By.XPATH, '//*[@id="openid-buttons"]/button[1]'))).click()

#     try:
#         WebDriverWait(driver, 60).until(EC.presence_of_element_located(
#             (By.ID, "Email"))).send_keys(username)      # Enters username
#     except TimeoutException:
#         del username
#         driver.quit()
#     WebDriverWait(driver, 60).until(EC.element_to_be_clickable(
#         (By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/form/div/div/input"))).click()      # Clicks NEXT
#     time.sleep(0.5)

#     try:
#         try:
#             WebDriverWait(driver, 60).until(EC.presence_of_element_located(
#                 (By.ID, "password"))).send_keys(password)       # Enters decoded Password
#         except TimeoutException:
#             driver.quit()
#         WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
#             (By.ID, "submit"))).click()     # Clicks on Sign-in
#     except TimeoutException or NoSuchElementException:
#         print('\nUsername/Password seems to be incorrect, please re-check\nand Re-Run the program.')
#         del username, password
#         driver.quit()

#     try:
#         WebDriverWait(driver, 60).until(lambda webpage: "https://stackoverflow.com/" in webpage.current_url)
#         print('\nLogin Successful!\n')
#     except TimeoutException:
#         print('\nUsername/Password seems to be incorrect, please re-check\nand Re-Run the program.')
#         del username, password
#         driver.quit()

# USERNAME = input("User Name : ")
# PASSWORD = str(getpass.getpass("\nenter password:\n"))      # A custom function for secured password input, explained at end.

# # Expected and required arguments added here.
# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_experimental_option('excludeSwitches', ['enable-logging'])

# # Assign drivers here.

# stealth(driver,
#         user_agent='DN',
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )       # Before Login, using stealth

# login(USERNAME, PASSWORD)       # Call login function/method

# stealth(driver,
#         user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )       # After logging in, revert back user agent to normal.

# # Redirecting to Google Meet Web-Page
# time.sleep(2)
# driver.execute_script("window.open('https://the website that you wanto to go.')")
# driver.switch_to.window(driver.window_handles[1])       # Redirecting to required from stackoverflow after logging in
# driver.switch_to.window(driver.window_handles[0])       # This switches to stackoverflow website
# driver.close()                                          # This closes the stackoverflow website
# driver.switch_to.window(driver.window_handles[0])       # Focuses on present website


# driver.find_element_by_id("CustomerEmail").send_keys(EMAIL)
# driver.find_element_by_id("CustomerPassword").send_keys(PASSWORD)
# driver.find_element_by_xpath("//input[@type='submit']").click()
# # idle 60s to solve capcha
# time.sleep(60)
# driver.refresh()
# driver.maximize_window()
# driver.get(link_to_run)
# boo = True
# # monitor + auto check out starts
# while boo:
#     try:
#         driver.get("https://www.deadstock.ca/cart/" +"39358978130005"+":1")
#         boo = False
#     except:
#         driver.refresh()
# time.sleep(600)


# def get_variants_id(early_link, size, lowerbound):
#     shoes_name = 'Air Jordan 3 Retro CT8532-030 Black - '+ str(size)
#     request = requests.get(early_link)
#     bs = bs4.BeautifulSoup(request.text, "html.parser")
#     scripts = bs.find_all("script")
#     i = 100
#     while i > 0:
#         for s in scripts:
#             try:
#                 if("var meta" in s.text):
#                     script = s.text
#                     script = script.split('"public_title":"' + str(lowerbound)+'","sku":')[1] #strip everything before SIZE
#                     script = script.split(',"price":24500,"name":"'+shoes_name+'","public_title":')[0] #strip everything after SIZE id
#                     script = script.split('"},{"id":')[1] #strip nun-integer
#                     return script
#             except:
#                 i -= 1
#     return "failed, variant id does not exit"


# #Generate early link for snkers
# def Generate_Early_Link(s, site):
#     link = ""
#     for char in s:
#         if(char == " " or char == "-"):
#             link += "-"
#         elif(char.isalpha() or char. isnumeric()):
#             link += char.lower()
#     return site+link


# def capusule_toronto_fetch():
#     LOG_IN = "https://www.capsuletoronto.com/account"
#     new_arrival_link = "https://www.capsuletoronto.com/collections/new-arrivals" #"https://www.capsuletoronto.com/collections/new-arrivals/footwear" #"https://www.capsuletoronto.com/products/air-jordan-11-low-ie-919712-023-black"#"https://nrml.ca/products/air-jordan-1-retro-high-og-555088-063" #"https://nrml.ca/products/w-nike-dunk-low-se-dd7099-001"
#     EMAIL = ""
#     PASSWORD = ""
#     driver = webdriver.Chrome(PATH)
#     driver.get(LOG_IN)
#     driver.find_element_by_id("CustomerEmail").send_keys(EMAIL)
#     driver.find_element_by_id("CustomerPassword").send_keys(PASSWORD)
#     driver.find_element_by_xpath("//input[@type='submit']").click()
#     time.sleep(60)
#     driver.refresh()
#     driver.maximize_window()
#     driver.get(new_arrival_link)
#     boo = True
#     while boo:
#         try:
#             driver.find_element_by_css_selector("a[href*='air-jordan-11-retro-ct8012-005']").click()
#             WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//label[@for="swatch-0-12"]'))).click()
#             WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "AddToCartText-product-template"))).click()
#             WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "agree"))).click()#Covid Agreement
#             WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, "checkout"))).click()
#             boo = False
#         except:
#             driver.refresh()
#     time.sleep(180)

# driver.find_elements_by_class_name("btn")
# j = 1
# for i in result:
#     print("-------------------------")
#     print(i.text + "-----------------------"+str(j))
#     j+=1
# driver.find_element_by_class_name("btn").send_keys(Keys.RETURN)
# driver.quit()
# recaptcha-checkbox-border
# shopify-challenge__button btn

# capusule_toronto_fetch()

# while boo:
#     try:
#         WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//label[@for="swatch-0-9"]'))).click()
#         WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "AddToCartText-product-template"))).click()
#         WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "agree"))).click()#Covid Agreement
#         WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, "checkout"))).click()
#         #driver.find_element_by_name("checkout").click()
#         boo = False
#     except:
#         driver.refresh()
# [link.get_attribute('href') for link in driver.find_elements_by_xpath('')]
# WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, keywords))).click()
# result = driver.find_elements_by_class_name("product-card")
# elems = driver.find_elements_by_xpath("//a[@href]")
# elems = driver.find_elements_by_xpath("//a[contains(@href, 'er-low-77-jumbo-dq1')]")
# elems.click()
# for elem in elems:
#     print("---------------------------")
#     #print(elem.get_attribute("href"))
#     print(elem)

# driver.get(LOG_IN)
# driver.find_element_by_id("CustomerEmail").send_keys(EMAIL)
# driver.find_element_by_id("CustomerPassword").send_keys(PASSWORD)
# driver.find_element_by_class_name("btn").click()
# driver.refresh()
# driver.get(LINK)
# driver.maximize_window()
# boo = True
# while boo:
#     try:
#         WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//label[@for="swatch-0-9"]'))).click()
#         WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "AddToCartText-product-template"))).click()
#         WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "agree"))).click()#Covid Agreement
#         WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, "checkout"))).click()
#         #driver.find_element_by_name("checkout").click()
#         boo = False
#     except:
#         driver.refresh()


# # Upcoming release calendar for sneaker site
# def pull_calendar(link):
#     driver.get(link)
#     calendar = []
#     if("deadstock" in link):
#         deadstock.deadstock_pull_calendar(driver, link, calendar)
#     elif("capsule" in link):
#         capsule_toronto.capsule_toronto_pull_calendar(driver, link, calendar)
#     elif("nrml" in link):
#         nrml.nrml_pull_calendar(driver, link, calendar)
#     print("---------------------------------------\nUpcoming Release\n---------------------------------------\n")
#     i = 1
#     for shoes in calendar:
#         print(str(i)+") "+shoes)
#         print("---------------------------------------\n")
#         i += 1
#     driver.quit()
#     return calendar


# driver.get("https://www.capsuletoronto.com/cart/39501394149411:1")

# # Get shoe id
# request = requests.get(CAPSULE)
# bs = bs4.BeautifulSoup(request.text, "html.parser")
# scripts = bs.find_all("script")
# # jsonObj = None
# SIZE = 9 #39501394116643
# SIZE_LOWER = 8.5


# L = "https://nrml.ca/products/air-jordan-1-retro-high-og-555088-063"

# def get_variants_id(early_link, size, lowerbound):
#     shoes_name = 'Air Jordan 3 Retro CT8532-030 Black - '+ str(size)
#     request = requests.get(early_link)
#     bs = bs4.BeautifulSoup(request.text, "html.parser")
#     scripts = bs.find_all("script")
#     i = 100
#     while i > 0:
#         for s in scripts:
#             try:
#                 if("var meta" in s.text):
#                     script = s.text
#                     script = script.split('"public_title":"' + str(lowerbound)+'","sku":')[1] #strip everything before SIZE
#                     script = script.split(',"price":24500,"name":"'+shoes_name+'","public_title":')[0] #strip everything after SIZE id
#                     script = script.split('"},{"id":')[1] #strip nun-integer
#                     return script
#             except:
#                 i -= 1
#     return "failed, variant id does not exit"

# driver.get('https://www.capsuletoronto.com/cart/'+ get_variants_id(CAPSULE, 10, 9.5)+':1')
# print('https://www.deadstock.ca/cart/'+ get_variants_id(deadstock, 10, 9.5)+':1')


# time.sleep(5)
# driver.quit

#         jsonStr = script
#         jsonObj = json.loads(jsonStr)

# for value in jsonObj["product"]["variants"]:
#     print ("ID: "+ str(value["id"]), "Size: " + str(value["public_title"]))


# # Get shoe id
# request = requests.get(CAPSULE)
# bs = bs4.BeautifulSoup(request.text, "html.parser")
# scripts = bs.find_all("script")
# jsonObj = None

# for s in scripts:
#     if "var meta" in s.text:
#         print("-----------------1")
#         print(s.text)
#         script = s.text
#         script = script.split("var meta = ")[1]
#         print("-----------------2")
#         print(script)
#         script = script.split(";\nfor (var attr in meta)")[0]
#         print("-----------------3")
#         print(script)

#         jsonStr = script
#         jsonObj = json.loads(jsonStr)

# for value in jsonObj["product"]["variants"]:
#     print ("ID: "+ str(value["id"]), "Size: " + str(value["public_title"]))


# #Generate early link for snkers
# def Generate_Early_Link(s, site):
#     link = ""
#     for char in s:
#         if(char == " "):
#             link += "-"
#         elif(char.isalpha() or char. isnumeric()):
#             link += char.lower()
#     return site+link


# confirm = input("NRML? Y/N")
# if(confirm.lower() == "y"):
#     CALENDAR_LINK = "https://nrml.ca/blogs/release-calendar"
#     driver.get(CALENDAR_LINK)
#     calendar = []
#     release_blog = driver.find_elements_by_class_name("font-heading")
#     for shoes in release_blog:
#         kicks = shoes.text
#         if(kicks == "NEWSLETTER"):
#             break
#         elif(kicks != "" and kicks != "RELEASE CALENDAR"):
#             kicks = kicks.strip()
#             calendar.append(kicks)
#     for shoes in calendar:
#         print(Generate_Early_Link(shoes, NRML))
#     driver.quit()
# elif(confirm.lower() == "n"):
#     print("exit")
#     exit
# else:
#     print("Error")
#     exit


# confirm = input("NRML? Y/N")
# if(confirm.lower() == "y"):
#     CALENDAR_LINK = "https://nrml.ca/blogs/release-calendar"
#     driver.get(CALENDAR_LINK)
#     calendar = []
#     release_blog = driver.find_elements_by_class_name("font-heading")
#     for shoes in release_blog:
#         kicks = shoes.text
#         if(kicks == "NEWSLETTER"):
#             break
#         elif(kicks != "" and kicks != "RELEASE CALENDAR"):
#             print(kicks)
#             calendar.append(kicks)

#     driver.quit()
# elif(confirm.lower() == "n"):
#     print("exit")
#     exit
# else:
#     print("Error")
#     exit


# #release calendar
# CALENDAR_LINK = "https://nrml.ca/blogs/release-calendar"
# driver.get(CALENDAR_LINK)
# calendar = []
# release_blog = driver.find_elements_by_class_name("font-heading")
# for shoes in release_blog:
#     kicks = shoes.text
#     if(kicks == "NEWSLETTER"):
#         break
#     elif(kicks != "" and kicks != "RELEASE CALENDAR"):
#         print(kicks)
#         calendar.append(kicks)
# driver.quit()


# driver.get(LOG_IN)
# email = driver.find_element_by_id("CustomerEmail")
# email.send_keys(EMAIL)
# password = driver.find_element_by_id("CustomerPassword")
# password.send_keys(PASSWORD)
# submit = driver.find_element_by_class_name("btn")
# ActionChains(driver).move_to_element(submit).click(submit).perform()
# driver.refresh()
# driver.get(LINK)
# boo = True
# while boo:
#     try:
#         driver.find_element_by_class_name("add-to-cart").click()
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
#         boo = False
#     except:
#         driver.refresh()


# # NRML login + auto checkout (Select size version)
# driver = webdriver.Chrome(PATH)
# SIZE = input("enter size: ")
# EMAIL = "sebyzy@gmail.com"
# PASSWORD = input("enter password:")
# LOG_IN = "https://nrml.ca/account"
# LINK = "https://nrml.ca/products/air-jordan-11-cmft-low-cw0784-001"#"https://nrml.ca/products/air-jordan-1-retro-high-og-555088-063" #"https://nrml.ca/products/w-nike-dunk-low-se-dd7099-001"
# driver.get(LOG_IN)
# driver.find_element_by_id("CustomerEmail").send_keys(EMAIL)
# driver.find_element_by_id("CustomerPassword").send_keys(PASSWORD)
# driver.find_element_by_class_name("btn").click()
# driver.refresh()
# driver.get(LINK)
# boo = True
# while boo:
#     try:
#         driver.find_element_by_id("Option1-"+str(SIZE)).click()
#         driver.find_element_by_class_name("add-to-cart").click()
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
#         boo = False
#     except:
#         driver.refresh()


# # NRML login + auto checkout
# driver = webdriver.Chrome(PATH)
# EMAIL = "sebyzy@gmail.com"
# PASSWORD = "" #input("enter password:")
# LOG_IN = "https://nrml.ca/account"
# LINK = "https://nrml.ca/products/w-nike-dunk-low-se-dd7099-001"#"https://nrml.ca/products/air-jordan-1-retro-high-og-555088-063" #"https://nrml.ca/products/w-nike-dunk-low-se-dd7099-001"
# driver.get(LOG_IN)
# driver.find_element_by_id("CustomerEmail").send_keys(EMAIL)
# driver.find_element_by_id("CustomerPassword").send_keys(PASSWORD)
# driver.find_element_by_class_name("btn").click()
# driver.refresh()
# driver.get(LINK)
# boo = True
# while boo:
#     try:
#         driver.find_element_by_class_name("add-to-cart").click()
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
#         boo = False
#     except:
#         driver.refresh()


# add_to_cart = driver.find_element_by_class_name("add-to-cart")
# ActionChains(driver).move_to_element(add_to_cart).click(add_to_cart).perform()


# boo = True
# while boo:
#     try:
#         add_to_cart = driver.find_element_by_class_name("add-to-cart")
#         ActionChains(driver).move_to_element(add_to_cart).click(add_to_cart).perform()
#         # try:
#         #     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
#         # finally:
#         #     boo = False

#     except:
#         driver.refresh()


# add_to_cart = driver.find_element_by_class_name("add-to-cart")
# ActionChains(driver).move_to_element(add_to_cart).click(add_to_cart).perform()
# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()


# #auto checkout NRML
# LINK = "https://nrml.ca/"#"https://nrml.ca/products/air-jordan-1-retro-high-og-555088-063" #"https://nrml.ca/products/w-nike-dunk-low-se-dd7099-001"
# driver.get(LINK)
# boo = True
# while boo:
#     try:
#         driver.find_element_by_class_name("add-to-cart").click()
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
#         boo = False
#     except:
#         driver.refresh()


# _11GJAaBiShTVGYuXppoYvE

##
# LiveStock

# NRML
# driver.get("https://nrml.ca/blogs/release-calendar")
# driver.get("https://www.techwithtim.net")
# Size CA
# driver.get("https://size.ca/products/jordan-1-retro-high-og-black-varsity-red-white")
# print(driver.title)
# search = driver.find_element_by_name("s")
# search = driver.find_element_by_partial_link_text('http://www.w3.org/2000/svg')
# search = driver.find_element_by_class_name("search-img")
# search_box_button= driver.find_element_by_class_name("search-img")
# #search = driver.find_element_by_id("search_box")
# ActionChains(driver).move_to_element(search_box_button).click(search_box_button).perform()
# search = driver.find_element_by_id("search_box")
# search.send_keys("jordan")
# search.send_keys(Keys.RETURN)

# time.sleep(5)

# driver.quit()
# print("DONEEEEEEEEEEEEE")

# #auto checkout early link method
# driver.get("https://www.deadstock.ca/products/adidas-originals-forum-84-low-cloud-white-team-power-red-cream-white")
# var_meta = driver

# driver.quit()

# #auto checkout deadstock
# size = input("size:")
# driver.get("https://www.deadstock.ca/products/adidas-originals-forum-84-low-cloud-white-team-power-red-cream-white?context=comingsoon")
# select_size = driver.find_element_by_id("ProductSelect-option-Size-"+size)
# add_to_cart = driver.find_element_by_id("AddToCart")
# ActionChains(driver).move_to_element(select_size).click(select_size).perform()
# ActionChains(driver).move_to_element(add_to_cart).click(add_to_cart).perform()
# time.sleep(5)

# driver.quit()


# # Search A Shoe
# driver.get("https://www.deadstock.ca/products/adidas-originals-forum-84-low-cloud-white-team-power-red-cream-white?context=comingsoon")
# search_box_button = driver.find_element_by_class_name("search-img")
# ActionChains(driver).move_to_element(search_box_button).click(search_box_button).perform()
# search = driver.find_element_by_id("search_box")
# search.send_keys("jordan")
# search.send_keys(Keys.RETURN)
# time.sleep(5)
# driver.quit()


# import time
# import getpass
# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException


# "https://www.newbalance.ca/en_ca/pd/made-in-usa-990v5/M990V5-21641.html#dwvar_M990V5-21641_size=10&dwvar_M990V5-21641_style=M990GL5&dwvar_M990V5-21641_width=D&pid=M990V5-21641&quantity=1"


# "https://www.newbalance.ca/en_ca/pd/550/BB550V1-34466.html"

# "dwvar_M990V5-21641_size="
# "dwvar_M990V5-21641_style="
# "dwvar_M990V5-21641_width="
# "pid="
# "quantity=1"
# "BB550PB1-D-04"
# "https://www.newbalance.ca/en_ca/pd/550/BB550V1-34466.html#dwvar_M990V5-21641_size=10&dwvar_BB550V1-34466_style=BB550PB1&dwvar_BB550V1-34466_width=D&pid=BB550V1-34466&quantity=1"


# def new_balance_ca_main(PATH):
#     driver = webdriver.Chrome(PATH)
#     driver.get("https://www.newbalance.ca/en_ca/nb-launches/")
#     calendar = []
#     release_blog = driver.find_elements_by_class_name(
#         "font-header-2")
#     for shoes in release_blog:
#         calendar.append(shoes.text)
#         print(shoes.text)
#     driver.quit()


# def test(PATH):
#     driver = webdriver.Chrome(PATH)
#     driver.get("https://www.newbalance.ca/en_ca/login/")
#     i = 0
#     while i <= 100:
#         driver.refresh()
#         time.sleep(10)
#         driver.find_element_by_id("login-form-email").send_keys("sebyzy@gmail.com")
#         driver.find_element_by_id("login-form-password").send_keys("zqSdxf_5.i@_HKS")
#         ActionChains(driver).move_to_element(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Login"]')))).click().perform()
#         time.sleep(10)
#         i+= 1

#     driver.get("https://www.newbalance.ca/en_ca/pd/327/MS327V1-36626.html#dwvar_MS327V1-36626_size=10.5&dwvar_MS327V1-36626_style=MS327WR1&dwvar_MS327V1-36626_width=D&pid=MS327V1-36626&quantity=1")
#     driver.maximize_window()
#     driver.refresh()
#     time.sleep(5)
#     # add =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[contains(@class,"button-label")]'))).click()
#     # driver.execute_script("add.click()")
#     # add_to_cart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#     #     (By.XPATH, '//span[contains(@class,"button-label")]')))
#    # time.sleep(10)
#     #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Add to Cart"]'))).click()

#     ActionChains(driver).move_to_element(WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Add to Cart"]')))).click().perform()
#     element = driver.find_element_by_xpath('//span[text()="Add to Cart"]')
#     driver.execute_script("element.click()")


#     #ActionChains(driver).move_to_element(WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Add to Cart"]')))).click().perform()
#     #ActionChains(driver).move_to_element(WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Add to Cart"]')))).click().perform()
#     #driver.find_element_by_xpath('//span[text()="Add to Cart"]').click()

#     # element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@class,"add-to-cart")]')))
#     # action = ActionChains(driver)
#     # action.click_and_hold(element)
#     # action.perform()
#     # action.release(element)
#     # #WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@class,"add-to-cart")]')))
#     #driver.execute_script("arguments[0].scrollIntoView();", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//button[contains(@class,"add-to-cart")]'))).click())
#     #ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "element_css")))).click().perform()

#     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "10.5"))).click()
#     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#     #     (By.XPATH, '//span[contains(@class,"button-label")]'))).click()
#     # add_to_cart = driver.find_element_by_css_selector('//button[contains(@class,"add-to-cart")]')

#     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#     #     (By.CLASS_NAME, "sales pr-2"))).click()
#     #driver.findElement(By.xpath("//span[contains(@class,'middle') and contains(text(), 'Next')]"))
#     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#     #     (By.CLASS_NAME, "paypal-button"))).click()
#     time.sleep(5)
#     driver.quit()


# test("/Users/seb/Chromedriver/chromedriver")


# # EMAIL = str(input("enter email:\n"))
# # PASSWORD = str(getpass.getpass("\nenter password:\n"))
# # keywords = str(input("\nenter search keywords:\n"))
# # size = str(input("\nenter size:\n"))
# # size = size.replace(".", "-") if "." in size else size
# # print("\nrunning...")
# # driver = webdriver.Chrome(PATH)
# # driver.get(LOG_IN)
# # driver.find_element_by_id("CustomerEmail").send_keys(EMAIL)
# # driver.find_element_by_id("CustomerPassword").send_keys(PASSWORD)
# # driver.find_element_by_xpath("//input[@type='submit']").click()
# # # idle 60s to solve capcha
# # time.sleep(60)
# # NEW_ARRIVAL_LINK = "https://www.capsuletoronto.com/collections/new-arrivals"
# # keywords = "air-jordan-1-retro-high-og"
# # driver.refresh()
# # driver.maximize_window()
# # driver.get(NEW_ARRIVAL_LINK)
# # boo = True
# # # monitor + auto check out starts
# # while boo:
# #     try:
# #         driver.find_element_by_css_selector(
# #             "a[href*='"+str(keywords)+"']").click()
# #         WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
# #             (By.XPATH, '//label[@for="swatch-0-' + str(size) + '"]'))).click()
# #         WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
# #             (By.ID, "AddToCartText-product-template"))).click()
# #         # Covid Agreement
# #         WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
# #             (By.ID, "agree"))).click()
# #         WebDriverWait(driver, 10).until(
# #             EC.visibility_of_element_located((By.NAME, "checkout"))).click()
# #         boo = False
# #     except:
# #         driver.refresh()
# # time.sleep(600)
