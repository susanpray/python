# -*- coding: utf-8 -*-
from userLogin import login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains
ipaddress = ["https://192.168.24.101/garuda/login.html","https://192.168.25.57/hawk/login.do","https://192.168.24.80/hawk/login.do"]
users = ["sysadmin","manager","normal","auditadmin"]
passwd = "polydata123!@#"

base_url = ipaddress[0]
user = users[0]
driver = webdriver.Firefox()
driver.implicitly_wait(30)

def ActionAddmail():
   login(driver,user,base_url)
   time.sleep(5)
   yigou=driver.find_element_by_xpath(u"//span[contains(text(), '全局设置')]")
   ActionChains(driver).move_to_element(yigou).perform()
   driver.find_element_by_link_text(u"通知管理").click()
   driver.find_element_by_id("paramSMTPReceiver").clear()
   driver.find_element_by_id("paramSMTPReceiver").send_keys("shaojuan.wang@polydata.com.cn")
   driver.find_element_by_id("paramSMTPSender").clear()
   driver.find_element_by_id("paramSMTPSender").send_keys("shaojuan.wang@polydata.com.cn")
   driver.find_element_by_id("paramSMTPServer").clear()
   driver.find_element_by_id("paramSMTPServer").send_keys("smtp.polydata.com.cn")
   driver.find_element_by_id("paramSMTPUser").clear()
   driver.find_element_by_xpath("//span/b[@role='presentation']").click()
   driver.find_element_by_xpath("//select/option[contains(text(),'不加密')]").click()
   #menu = driver.find_element_by_xpath("//div/following-sibling::span[contain(text(),'不加密')")
   #webdriver.ActionChains(driver).move_to_element(menu).perform()
   #driver.find_element_by_xpath("//div/following-sibling::span[contain(text(),'不加密')").click()
   driver.find_element_by_id("paramSMTPUser").send_keys("shaojuan.wang")
   driver.find_element_by_id("paramSMTPPassword").clear()
   driver.find_element_by_id("paramSMTPPassword").send_keys("Juanjuan88")
   driver.find_element_by_id("subBut").click()
   driver.find_element_by_xpath("//button[contains(text(),'确定')]").click()

   time.sleep(5)

   #driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
   #driver.find_element_by_xpath("//ol[@id='paramCategory']/li[2]/div").click()
   driver.find_element_by_xpath("//div[contains(text(),'Syslog服务器')]").click()
   time.sleep(2)
   driver.find_element_by_id("paramSyslogServer1").clear()
   driver.find_element_by_id("paramSyslogServer1").send_keys("192.168.24.106")
   driver.find_element_by_id("subBut").click()
   driver.find_element_by_xpath("//button[contains(text(),'确定')]").click()

   time.sleep(5)
   # driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
   # driver.find_element_by_xpath("//ol[@id='paramCategory']/li[3]/div").click()
   driver.find_element_by_xpath("//div[contains(text(),'SNMP服务器')]").click()
   driver.find_element_by_id("paramSNMPServer").clear()
   time.sleep(2)
   driver.find_element_by_id("paramSNMPServer").send_keys("192.168.24.106")
   driver.find_element_by_id("parmaSNMPServerPort").clear()
   driver.find_element_by_id("parmaSNMPServerPort").send_keys("162")
   driver.find_element_by_id("paramSNMPEnterprise").clear()
   driver.find_element_by_id("paramSNMPEnterprise").send_keys("1.3.6.1.4.1.45487")
   driver.find_element_by_id("paramSNMPOID").clear()
   driver.find_element_by_id("paramSNMPOID").send_keys("1.3.4.1.2.3.1")
   driver.find_element_by_id("subBut").click()
   #driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
   driver.find_element_by_xpath("//button[contains(text(),'确定')]").click()

ActionAddmail()