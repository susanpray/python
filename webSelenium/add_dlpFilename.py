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

def add_dlpfile():
        dlpdict= {"filenameNoIP":u"文件.txt"}

        for key in dlpdict.keys():
                login(driver,user,base_url)
                dlpname = str(key)
                value = dlpdict.get(key)
                time.sleep(3)
                yigou=driver.find_element_by_xpath(u"//span[contains(text(), '策略管理')]")
                ActionChains(driver).move_to_element(yigou).perform()
                driver.find_element_by_xpath("//a[@href='#/policy/manager']").click()
                time.sleep(3)
                driver.find_element_by_xpath(u"//div[contains(text(), 'DLP策略')]").click()
                driver.find_element_by_xpath(u"//span[contains(text(), '新增')]").click()
                driver.find_element_by_id("policyname").clear()
                driver.find_element_by_id("policyname").send_keys("%s" %(dlpname))
                time.sleep(2)
                driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
                driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
                select = Select(driver.find_element_by_xpath(u"//select[contains(@id, 'policytype_')]"))
                select.select_by_visible_text(u"文件名")
                driver.find_element_by_xpath(u"//div[@class='col-md-8']/div[@class='form-group']/input").send_keys("%s" %(value))
                time.sleep(3)
                driver.find_element_by_xpath(u"//span[contains(text(),'生成安全事件')]").click()
                driver.find_element_by_id("alertname").send_keys("%s" %(dlpname))
                Select(driver.find_element_by_id("alertseverity")).select_by_visible_text(u"极度严重")
                Select(driver.find_element_by_id("alertcategory")).select_by_visible_text(u"有害程序")
                driver.find_element_by_css_selector("#alertcategory > option.ng-binding.ng-scope").click()
                Select(driver.find_element_by_id("alertsubcategory")).select_by_visible_text(u"网页恶意代码")
                #driver.find_element_by_css_selector("option[value=\"1102\"]").click()
                #driver.find_element_by_xpath("//form[@id='dataForm']/div[2]/div[10]/button[2]").click()
                driver.find_element_by_xpath(u"//div/button[contains(text(), '提交')]").click()
                time.sleep(5)
if __name__ == "__main__":
    add_dlpfile()