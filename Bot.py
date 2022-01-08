from requests.models import CONTENT_CHUNK_SIZE, requote_uri
from selenium.webdriver.remote.webelement import WebElement
import capsule_toronto
import deadstock
import nrml
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


PATH = "/Users/seb/Chromedriver/chromedriver"


def bot_configure(retailer):
    if(retailer == "a"):
        nrml.nrml_main(PATH)
    elif(retailer == "b"):
        deadstock.deadstock_main(PATH)
    elif(retailer == "c"):
        capsule_toronto.capsule_toronto_main(PATH)





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
    #[link.get_attribute('href') for link in driver.find_elements_by_xpath('')]
    #WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, keywords))).click()
    #result = driver.find_elements_by_class_name("product-card")
    #elems = driver.find_elements_by_xpath("//a[@href]")
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
#print('https://www.deadstock.ca/cart/'+ get_variants_id(deadstock, 10, 9.5)+':1')


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


#add_to_cart = driver.find_element_by_class_name("add-to-cart")
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


#add_to_cart = driver.find_element_by_class_name("add-to-cart")
# ActionChains(driver).move_to_element(add_to_cart).click(add_to_cart).perform()
#WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()


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
#search = driver.find_element_by_name("s")
#search = driver.find_element_by_partial_link_text('http://www.w3.org/2000/svg')
#search = driver.find_element_by_class_name("search-img")
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
