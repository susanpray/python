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
ipaddress = ["https://192.168.24.101/garuda/login.html","https://192.168.25.57/hawk/login.do","https://192.168.24.80/hawk/login.do"]
users = ["sysadmin","manager","normal","auditadmin"]
passwd = "polydata123!@#"

base_url = ipaddress[0]
user = users[0]
driver = webdriver.Firefox()
driver.implicitly_wait(30)
ipname = "192.0.0.0"
mname = "mining22"

def AddMining():
    login(driver,user,base_url)
    time.sleep(5)
    yigou=driver.find_element_by_xpath(u"//span[contains(text(), '策略管理')]")
    ActionChains(driver).move_to_element(yigou).perform()
    driver.find_element_by_xpath("//a[@href='#/policy/manager']").click()
    time.sleep(3)
    driver.find_element_by_xpath(u"//div[contains(text(), '挖掘策略')]").click()
    time.sleep(3)
    driver.find_element_by_xpath(u"//a//span[contains(text(), '新增')]").click()
    driver.find_element_by_id("policyname").clear()
    driver.find_element_by_id("policyname").send_keys("%s" %(mname))
    Select(driver.find_element_by_id("policytype")).select_by_visible_text(u"普通会话连接归并")
    driver.find_element_by_xpath(u"//span[contains(text(), '忽略D和E类网络')]").click()
    driver.find_element_by_xpath(u"//span[contains(text(), '忽略广播包')]").click()

    Select(driver.find_element_by_id("direction")).select_by_visible_text(u"内网至内网")
    driver.find_element_by_xpath("(//option[@value='3'])[3]").click()
    Select(driver.find_element_by_id("addressscope")).select_by_visible_text(u"基于IP地址")
    driver.find_element_by_xpath(u"//select[@id='sourceaddress']/option[contains(text(), '%s')]" %(ipname)).click()
    driver.find_element_by_xpath(u"//select[@id='destinationaddress']/option[contains(text(), '%s')]" %(ipname)).click()

    driver.find_element_by_id("count").clear()
    driver.find_element_by_id("count").send_keys("1")
    driver.find_element_by_xpath(u"//select[@id='mergefield']/option[contains(text(), '源地址')]").click()
    driver.find_element_by_xpath(u"//select[@id='mergefield']/option[contains(text(), '目的地址')]").click()
    driver.find_element_by_xpath(u"//select[@id='mergefield']/option[contains(text(), '目的端口')]").click()
    driver.find_element_by_xpath(u"//select[@id='mergefield']/option[contains(text(), '协议')]").click()
    driver.find_element_by_xpath(u"//select[@id='mergefield']/option[contains(text(), '应用协议')]").click()

    driver.find_element_by_xpath(u"//span[contains(text(),'生成安全事件')]").click()
    driver.find_element_by_id("alertname").clear()
    driver.find_element_by_id("alertname").send_keys("%s" %(mname))
    Select(driver.find_element_by_id("alertseverity")).select_by_visible_text(u"极度严重")
    Select(driver.find_element_by_id("alertcategory")).select_by_visible_text(u"网络攻击")
    driver.find_element_by_xpath("//option[@value='1002']").click()
    Select(driver.find_element_by_id("alertsubcategory")).select_by_visible_text(u"拒绝服务攻击")
    #driver.find_element_by_css_selector("option[value=\"1108\"]").click()
    #driver.find_element_by_xpath("//form[@id='dataForm']/div[2]/div[19]/button[2]").click()
    driver.find_element_by_xpath(u"//div/button[contains(text(), '提交')]").click()

AddMining()
driver.quit()
