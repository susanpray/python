# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains
from easyExcel import *
import random
import sys
import win32com
from win32com.client import constants, Dispatch

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.24.6.90/testlink/login.php"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.fileb = u"E:\\测\\日报模板.xlsx"


   # def para(self,suite1):
 #       driver = self.driver
#         self.NotRun=driver.find_element_by_xpath(u"//span[contains(text(),'%s')]/span[@title='尚未执行']"%suite1).text
#         self.PassCase=driver.find_element_by_xpath(u"//span[contains(text(),'%s')]/span[@title='通过']"%suite1).text
#        self.Fail=driver.find_element_by_xpath(u"//span[contains(text(),'%s')]/span[@title='失败']"%suite1).text
#        self.Navailable=driver.find_element_by_xpath(u"//span[contains(text(),'%s')]/span[@title='无效']"%suite1).text
#         self.Block=driver.find_element_by_xpath(u"//span[contains(text(),'%s')]/span[@title='锁定']"%suite1).text

    def plan_build(self,test_plan1,build1):
        driver = self.driver
        driver.find_element_by_name("setting_testplan").find_element_by_xpath("//option[@label='%s']"%test_plan1).click()
        driver.find_element_by_name("setting_build").find_element_by_xpath("//option[@label='%s']"%build1).click()
        #driver.get_screenshot_as_file("E:\\python script\\testlink\\testlink.png")
        driver.find_element_by_xpath("//div[@id='ext-gen8']").click()
        #driver.find_element_by_xpath(u"//span[contains(text(),'前台')]")

    def write_excel(self,row,suite1):
        fileb = self.fileb
        xls = easyExcel(fileb)
        col = ['e','f','g','h','i']
        driver = self.driver
        NotRun=driver.find_element_by_xpath(u"//span[contains(text(),'%s')]/span[@title='尚未执行']"%suite1).text
        PassCase=driver.find_element_by_xpath(u"//span[contains(text(),'%s')]/span[@title='通过']"%suite1).text
        Fail=driver.find_element_by_xpath(u"//span[contains(text(),'%s')]/span[@title='失败']"%suite1).text
        Navailable=driver.find_element_by_xpath(u"//span[contains(text(),'%s')]/span[@title='无效']"%suite1).text
        Block=driver.find_element_by_xpath(u"//span[contains(text(),'%s')]/span[@title='锁定']"%suite1).text
        for x in col:
            if x == 'e':
              xls.setCell('sheet2',row,'e',PassCase.split(','))
            elif x == 'f':
              xls.setCell('sheet2',row,'f',Fail.split(','))
            elif x == 'g':
              xls.setCell('sheet2',row,'g',Navailable.split(','))
            elif x == 'h':
              xls.setCell('sheet2',row,'h',Block.split(','))
            else:
              xls.setCell('sheet2',row,'i',NotRun.split(','))
        xls.save()
        xls.close()

    
    def test_login(self):
        test_plans =[u'功能','firefox','IE']
        builds = [u'SIT第一轮',u'SIT第二轮']
        suites = [u'前台',u'后台',u'兼容']
        #fileb = self.fileb
        #xls = easyExcel(fileb)
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("admin")
        driver.find_element_by_name("tl_password").clear()
        driver.find_element_by_name("tl_password").send_keys("admin")
        driver.find_element_by_name("login_submit").click()
        time.sleep(10)
        driver.switch_to_frame("titlebar")
        driver.find_element_by_link_text(u"执行").click()
        driver.switch_to_default_content()
        driver.switch_to_frame("mainframe")
        driver.switch_to_frame("treeframe")
        for test_plan in test_plans:
            for build in builds:
                for suite in suites:
                    if test_plan == u'功能'and build ==u'SIT第一轮'and suite == u'前台':
                       #self.para(suite)
                       self.plan_build(test_plan,build)
                       self.write_excel(4,suite)
                    elif test_plan == u'功能'and build == u'SIT第一轮'and suite == u'后台':
                       #self.para(suite)
                       self.plan_build(test_plan,build)
                       self.write_excel(5,suite)
                    elif test_plan == 'firefox'and build == u'SIT第一轮'and suite == u'兼容':
                       #self.para(suite)
                       self.plan_build(test_plan,build)
                       self.write_excel(2,suite)
                    elif test_plan == 'IE'and build == u'SIT第一轮'and suite == u'兼容':
                       #self.para(suite)
                       self.plan_build(test_plan,build)
                       self.write_excel(3,suite)
                    else:
                       continue




    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
