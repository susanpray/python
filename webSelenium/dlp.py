# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains

class Dlp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://192.168.24.101/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def login(self):
        driver = self.driver
        driver.get(self.base_url + "/garuda/login.html")
        #driver.find_element_by_css_selector("#menu3 > ul > li.active > a").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("sysadmin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("polydata123!@#")
        driver.find_element_by_id("validatecode").clear()
        driver.find_element_by_id("validatecode").send_keys("7750")
        time.sleep(10)
        driver.maximize_window()

    def add_dlp(self):
        def login()
        driver.find_element_by_id("subBut").click()
        yigou=driver.find_element_by_xpath(u"//span[contains(text(), '策略管理')]")
        ActionChains(driver).move_to_element(yigou).perform()
        #driver.find_element_by_css_selector("#menu3 > ul > li > a").click()
        #driver.find_element_by_xpath("//ol[@id='paramCategory']/li[12]/div").click()
        driver.find_element_by_xpath("//a[@href='#/policy/manager']").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"//div[contains(text(), 'DLP策略')]").click()
        time.sleep(2)
        driver.find_element_by_xpath(u"//span[contains(text(), '新增')]").click()
        driver.find_element_by_id("policyname").clear()
        driver.find_element_by_id("policyname").send_keys("dlp111")
        time.sleep(5)
        driver.find_element_by_id("s2id_autogen1").click()
        driver.find_element_by_xpath(u"//select[@id='sourceaddress']/option[contains(text(), '192.168')]").click()
        driver.find_element_by_id("s2id_autogen2").click()
        driver.find_element_by_xpath(u"//select[@id='destinationaddress']/option[contains(text(), '192.168')]").click()
        time.sleep(5)
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        driver.find_element_by_xpath(u"//div[@class='col-md-8']/div[@class='form-group']/input").send_keys("^###")
        ####select
        select = Select(driver.find_element_by_xpath(u"//select[contains(@id, 'isRule_')]"))
        select.select_by_visible_text(u"是")
        time.sleep(3)
        driver.find_element_by_xpath(u"//span[contains(text(),'生成安全事件')]").click()
        driver.find_element_by_id("alertname").send_keys("dlp111")
        Select(driver.find_element_by_id("alertseverity")).select_by_visible_text(u"极度严重")
        Select(driver.find_element_by_id("alertcategory")).select_by_visible_text(u"有害程序")
        driver.find_element_by_css_selector("#alertcategory > option.ng-binding.ng-scope").click()
        Select(driver.find_element_by_id("alertsubcategory")).select_by_visible_text(u"网页恶意代码")
        driver.find_element_by_css_selector("option[value=\"1102\"]").click()
        driver.find_element_by_xpath("//form[@id='dataForm']/div[2]/div[10]/button[2]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
