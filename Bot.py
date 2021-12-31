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
NRML = "https://nrml.ca/products/"
DEADSTOCK = "https://www.deadstock.ca/products/jordan-1-centre-court-white-military-blue"  #"https://www.deadstock.ca/cart/"


# Get shoe id
request = requests.get(DEADSTOCK)
bs = bs4.BeautifulSoup(request.text, "html.parser")
scripts = bs.find_all("script")
jsonObj = None

for s in scripts:
    if "var meta" in s.text:
        print("-----------------")
        print(s.text)
        script = s.text
        script = script.split("var meta = ")[1]
        script = script.split(";\nfor (var attr in meta)")[0]

        jsonStr = script
        jsonObj = json.loads(jsonStr)

for value in jsonObj["product"]["variants"]:
    print ("ID: "+ str(value["id"]), "Size: " + str(value["public_title"]))
    

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
#ActionChains(driver).move_to_element(add_to_cart).click(add_to_cart).perform()


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
#ActionChains(driver).move_to_element(add_to_cart).click(add_to_cart).perform()
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

    


#_11GJAaBiShTVGYuXppoYvE

##
# LiveStock

# NRML
#driver.get("https://nrml.ca/blogs/release-calendar")
#driver.get("https://www.techwithtim.net")
# Size CA
#driver.get("https://size.ca/products/jordan-1-retro-high-og-black-varsity-red-white")
#print(driver.title) 
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


