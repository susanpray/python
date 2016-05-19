# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains

ipaddress = ["https://192.168.24.101/garuda/login.html","https://192.168.25.57/hawk/login.do","https://192.168.24.80/hawk/login.do"]
users = ["sysadmin","manager","normal","auditadmin"]
passwd = "polydata123!@#"

base_url = ipaddress[0]
user = users[0]
#userCreate = users[2]

#driver = webdriver.Firefox()
#driver.implicitly_wait(30)

def login(driver,user,base_url):
        driver.get(base_url)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("%s" %(user))
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("%s" %(passwd))
        #driver.find_element_by_id("validatecode").clear()
        #driver.find_element_by_id("validatecode").send_keys("7750")
        time.sleep(10)
        driver.maximize_window()
        driver.find_element_by_id("subBut").click()
        #time.sleep(3600)

#login(user,base_url)