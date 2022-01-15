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

UPCOMING_RELEASES = "https://www.nike.com/ca/launch?s=upcoming"
EARLY_LINK = ""
RELEASE_TITLE = ""


def snkrs_main(PATH):
    # EMAIL = str(input("enter email:\n"))
    # PASSWORD = str(getpass.getpass("\nenter password:\n"))
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.nike.com/ca/launch?s=upcoming")
    driver.find_element_by_xpath("//button[normalize-space()='Join/Log In']").click()
    driver.find_element_by_xpath("//lable[normalize-space()='Email address]").send_keys("Sebyzy@gmail.com")

    


    time.sleep(600)

snkrs_main("/Users/seb/Chromedriver/chromedriver")