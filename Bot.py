import imp
import capsule_toronto
import deadstock
import nrml
import size_ca
import crtsd_snkrs
import nomad
import getpass
import selenium
import bs4
import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

PATH = "/Users/seb/Chromedriver/chromedriver"
PROFILE_PATH = "/Users/seb/Library/Application Support/Google/Chrome/Default"


def bot_configure(RETAILER):
    EMAIL = str(input("enter email:\n"))
    PASSWORD = str(getpass.getpass("\nenter password:\n"))
    if(RETAILER == "a"):
        nrml.nrml_main(PATH, EMAIL, PASSWORD)
    elif(RETAILER == "b"):
        deadstock.deadstock_main(PATH, PROFILE_PATH)
    elif(RETAILER == "c"):
        capsule_toronto.capsule_toronto_main(PATH,PROFILE_PATH)
    elif(RETAILER == "d"):
        size_ca.size_ca_main(PATH, EMAIL, PASSWORD)
    elif(RETAILER == "e"):
        crtsd_snkrs.crtsd_snkrs_main(PATH, EMAIL, PASSWORD)
    elif(RETAILER == "f"):
        nomad.nomad_main(PATH, EMAIL, PASSWORD)

