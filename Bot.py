import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/seb/Chromedriver/chromedriver"
driver = webdriver.Chrome(PATH)

 
#auto checkout NRML
driver.get("https://nrml.ca/products/w-nike-dunk-low-se-dd7099-001")
add_to_cart = driver.find_element_by_class_name("add-to-cart")
ActionChains(driver).move_to_element(add_to_cart).click(add_to_cart).perform()
try:
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='ShopifyPay-button'][role='button']"))).click()
    
finally:
    print("DONEEEEEEEEE")
    driver.quit() 



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


