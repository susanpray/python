# -*- coding: utf-8 -*-
from userLogin import login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains
ipaddress = "https://192.168.24.101/garuda/login.html"
users = "sysadmin"
passwd = "polydata123!@#"

base_url = ipaddress
user = users
driver = webdriver.Firefox()
driver.implicitly_wait(30)
mname =("mining11","mining22")
def del_mining():
    login(driver,user,base_url)
    time.sleep(3)
    yigou=driver.find_element_by_xpath(u"//span[contains(text(), '策略管理')]")
    ActionChains(driver).move_to_element(yigou).perform()
    driver.find_element_by_xpath("//a[@href='#/policy/manager']").click()
    time.sleep(3)
    driver.find_element_by_xpath(u"//div[contains(text(), '挖掘策略')]").click()
    for name in mname:
        driver.find_element_by_xpath(u"//td[@title='%s']/preceding-sibling::td/input[@type='checkbox']" %(name)).click()
    driver.find_element_by_xpath(u"//span[contains(text(), '删除')]").click()
    driver.find_element_by_xpath(u"//div/button[contains(text(), '确认')]").click()
    time.sleep(5)

if __name__ == "__main__":
    del_mining()
    driver.quit()