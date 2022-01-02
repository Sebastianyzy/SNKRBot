
UPCOMING_RELEASES = "https://www.capsuletoronto.com/pages/launches"
EARLY_LINK = "https://www.capsuletoronto.com/products/"
RELEASE_TITLE = "address"


def capsule_bot_configure(calendar, shoes):
    color = input("enter color:\n")
    return capsule_generate_early_link(calendar[shoes-1], EARLY_LINK, str(color))  


def capsule_generate_early_link(s, site, color):
    link = ""
    s.lstrip()
    s.rstrip()
    for char in s: 
        if(char == " " or char == "-"):
            link += "-"
        elif(char.isalpha() or char. isnumeric()):
            link += char.lower() 
    return site+link+color


def capsule_toronto_pull_calendar(driver, link, calendar):   
    driver.get(link)
    release_blog = driver.find_elements_by_class_name(RELEASE_TITLE)
    for shoes in release_blog:
        calendar.append(shoes.text)
    return calendar



  
# #Capsule auto checkout
# driver = Bot.webdriver.Chrome(Bot.PATH)
# #driver.get(LOG_IN)
# LINK = "https://www.capsuletoronto.com/products/air-jordan-11-low-ie-919712-023-black"#"https://nrml.ca/products/air-jordan-1-retro-high-og-555088-063" #"https://nrml.ca/products/w-nike-dunk-low-se-dd7099-001"
# #driver.get(LOG_IN)
# #driver.find_element_by_id("CustomerEmail").send_keys(EMAIL)
# #driver.find_element_by_id("CustomerPassword").send_keys(PASSWORD)
# #driver.find_element_by_class_name("btn").click()
# #driver.refresh()
# driver.get(LINK)
# driver.maximize_window()
# boo = True
# while boo:
#     try:       
#         Bot.WebDriverWait(driver, 3).until(Bot.EC.visibility_of_element_located((Bot.By.XPATH, '//label[@for="swatch-0-9"]'))).click()
#         Bot.WebDriverWait(driver, 2).until(Bot.EC.visibility_of_element_located((Bot.By.ID, "AddToCartText-product-template"))).click()
#         Bot.WebDriverWait(driver, 2).until(Bot.EC.visibility_of_element_located((Bot.By.ID, "agree"))).click()#Covid Agreement   
#         Bot.WebDriverWait(driver, 2).until(Bot.EC.visibility_of_element_located((Bot.By.NAME, "checkout"))).click()
#         #driver.find_element_by_name("checkout").click()
#         boo = False
#     except:
#         driver.refresh()