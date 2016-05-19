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

driver = webdriver.Firefox()
driver.implicitly_wait(30)

def login(user,base_url):
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

def IPadd(user,base_url,sourceIp,destIp):
        login(user,base_url)
        yigou=driver.find_element_by_xpath(u"//span[contains(text(), '对象管理')]")
        ActionChains(driver).move_to_element(yigou).perform()

        driver.find_element_by_xpath("//a[@href='#/object/ipaddress']").click()
        time.sleep(3)
        driver.find_element_by_xpath(u"//span[contains(text(), '新增')]").click()
        driver.find_element_by_css_selector("div.form-group > #instancename").clear()
        driver.find_element_by_css_selector("div.form-group > #instancename").send_keys("%s" %(sourceIp))
        Select(driver.find_element_by_id("reserved2")).select_by_visible_text(u"是")
        driver.find_element_by_xpath("(//option[@value='1'])[3]").click()
        Select(driver.find_element_by_id("reserved9")).select_by_visible_text(u"开启")
        driver.find_element_by_xpath("(//option[@value='1'])[4]").click()
        driver.find_element_by_id("reserved6").clear()
        driver.find_element_by_id("reserved6").send_keys("%s" %(sourceIp))
        driver.find_element_by_id("reserved8").clear()
        driver.find_element_by_id("reserved8").send_keys("%s" %(destIp))
        #driver.find_element_by_xpath("//form[@id='groupForm']/div[3]/button[2]").click()
        #driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath(u"//div/button[contains(text(), '提交')]").click()

IPadd(user,base_url,"192.0.0.0","192.255.255.255")
driver.quit()