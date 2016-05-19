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
#users = "sysadmin"
passwd = "polydata123!@#"
base_url = ipaddress
driver = webdriver.Firefox()
driver.implicitly_wait(30)
users = ["sysadmin","manager","normal","susanadmin"]
user = users[3]

dlpdict= {"11":u"\d分钟\W","22":"cat(aract|erpillar|)"}

def add_dlp():
    login(driver,user,base_url)
    time.sleep(5)
    yigou=driver.find_element_by_xpath(u"//span[contains(text(), '策略管理')]")
    ActionChains(driver).move_to_element(yigou).perform()
    driver.find_element_by_xpath("//a[@href='#/policy/manager']").click()
    time.sleep(3)
    driver.find_element_by_xpath(u"//div[contains(text(), 'DLP策略')]").click()
    time.sleep(5)
    for key in dlpdict.keys():
        dlpname = 'dlp00'+ str(key)
        value = dlpdict.get(key)
        driver.find_element_by_xpath(u"//span[contains(text(), '新增')]").click()
        driver.find_element_by_id("policyname").clear()
        driver.find_element_by_id("policyname").send_keys("%s" %(dlpname))
        time.sleep(5)
        #driver.find_element_by_xpath("//div[@id='s2id_sourceaddress']/ul/li/input[@id='s2id_autogen1']").click()
        driver.find_element_by_xpath(u"//select[@id='sourceaddress']/option[contains(text(), '192.0.0.0')]").click()
        #driver.find_element_by_xpath("//div[@id='s2id_destinationaddress']/ul/li/input[@id='s2id_autogen2']").click()
        driver.find_element_by_xpath(u"//select[@id='destinationaddress']/option[contains(text(), '192.0.0.0')]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        driver.find_element_by_xpath(u"//div[@class='col-md-8']/div[@class='form-group']/input").send_keys("%s" %(value))
        ####select
        select = Select(driver.find_element_by_xpath(u"//select[contains(@id, 'isRule_')]"))
        select.select_by_visible_text(u"是")
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
        time.sleep(4)


if __name__ == "__main__":
    add_dlp()
    driver.quit()
