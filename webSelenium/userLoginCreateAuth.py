# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

base_url = "https://192.168.24.101/garuda/login.html"
user = "sysadmin"
passwd = "polydata123!@#"
memberAll = ("normal","manager","susanadmin")

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
        #time.sleep(360)

def createUser(userCreate,usetype):
        login(user,base_url)
        yigou=driver.find_element_by_xpath(u"//span[contains(text(), '全局设置')]")
        ActionChains(driver).move_to_element(yigou).perform()
        driver.find_element_by_xpath("//a[@href='#/system/user']").click()
        time.sleep(3)
        driver.find_element_by_xpath(u"//span[contains(text(), '新增')]").click()
        driver.find_element_by_id("loginname").clear()
        driver.find_element_by_id("loginname").send_keys("%s" %(userCreate))
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("%s" %(userCreate))
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("polydata123!@#")
        driver.find_element_by_id("confirmPwd").clear()
        driver.find_element_by_id("confirmPwd").send_keys("polydata123!@#")
        Select(driver.find_element_by_xpath("//form[@id='dataForm']/div[2]/div[3]/div[2]/div/select")).select_by_visible_text("%s" %(usetype))
        driver.find_element_by_id("telephone").clear()
        driver.find_element_by_id("telephone").send_keys("025-48425509")
        driver.find_element_by_id("mobilephone").clear()
        driver.find_element_by_id("mobilephone").send_keys("13951726248")
        driver.find_element_by_id("jobnum").clear()
        driver.find_element_by_id("jobnum").send_keys("785454")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("susan@hotmail.com")
        #driver.find_element_by_xpath(u"//div[@class='form-group']/div/div[2]/label/span]").click()
        #driver.find_element_by_id("verifyipcheckbox").click()
        driver.find_element_by_xpath("//form[@id='dataForm']/div[2]/div[6]/div/div/div/div[2]/label/span").click()
        driver.find_element_by_id("startstandardip").clear()
        driver.find_element_by_id("startstandardip").send_keys("192.168.24.166")
        driver.find_element_by_id("endstandardip").clear()
        driver.find_element_by_id("endstandardip").send_keys("192.168.24.166")
        driver.find_element_by_id("description").clear()
        driver.find_element_by_id("description").send_keys("dddd")
        #driver.find_element_by_xpath("//form[@id='dataForm']/div[3]/button[2]").click()
        driver.find_element_by_xpath(u"//div/button[contains(text(), '提交')]").click()
        time.sleep(5)

def authUser(userCreate,subsys,userole):
        login(user,base_url)
        yigou=driver.find_element_by_xpath(u"//span[contains(text(), '全局设置')]")
        ActionChains(driver).move_to_element(yigou).perform()
        driver.find_element_by_xpath("//a[@href='#/system/user']").click()
        time.sleep(3)
        #driver.find_element_by_xpath(u"//td[@title='%s']/following-sibling::td/a[contains(text(),'子系统授权')]" %(userCreate)).click()
        driver.find_element_by_xpath(u"//td[@title='%s']/following-sibling::td/input[@value='子系统授权']" %(userCreate)).click()
        driver.find_element_by_xpath(u"//a[contains(@title,'%s')]/following-sibling::ul/li[%d]/span[2]" %(subsys,userole)).click()

        time.sleep(5)
        #driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_xpath(u"//div/button[contains(text(), '提交')]").click()

def DeleteUser(userdel):
        login(user,base_url)
        yigou=driver.find_element_by_xpath(u"//span[contains(text(), '全局设置')]")
        ActionChains(driver).move_to_element(yigou).perform()
        driver.find_element_by_xpath("//a[@href='#/system/user']").click()
        time.sleep(3)
        driver.find_element_by_xpath(u"//td[@title='%s']/preceding-sibling::td/input[@type='checkbox']" %(userdel)).click()
        driver.find_element_by_xpath(u"//span[contains(text(),'删除')]").click()
        driver.find_element_by_xpath(u"//button[contains(text(),'确认')]").click()

def close_alert_and_get_its_text():
        accept_next_alert = True
        try:
            alert = driver.switch_to_alert()
            alert_text = alert.text
            if accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: accept_next_alert = True




###########创建用户#######################################
def createUserMutiple():
        memberdict = {"normal":u"普通用户","manager":u"管理员","susanadmin":u"系统管理员"}
        for member in memberdict.keys():
                print member
                print memberdict.get(member)
                createUser(member,memberdict.get(member))

###########授权用户#######################################
def authUserMutilpe():
        for address in ["192.168.24.91","192.168.24.92","192.168.25.71"]:
                authUser("manager",address,int(2))
                authUser("normal",address,int(3))
                authUser("susanadmin",address,int(1))

###########登录#############################################
def loginMultipleSubsystem():
        linklist1 = ('https://192.168.25.71/pangolin/login.html','https://192.168.24.91/hawk/login.do')
        for member in memberAll:
               for link in linklist1:
                       try:
                                login(member,link)
                                alert=driver.switch_to_alert()
                                print member +" in "+ link +" is "+ alert.text
                                alert.accept()
                                print("Alert accepted")
                       except NoAlertPresentException:
                                pass
                                print "no alert is existed,%s login successfully to %s"%(member,link)
                       time.sleep(150)

def loginMultipleSoc():

        linklist2 = 'https://192.168.24.101/garuda/login.html'

        for member in memberAll:

               try:
                       login(member,linklist2)
                       time.sleep(3)
                      # if driver.find_element_by_xpath(u"//div[@class='modal-content']"):
                       prompt = driver.find_element_by_xpath(u"//div[@class='modal-body text-info ng-binding ng-scope']").text
                       print "%s login to %s failed:%s"%(member,linklist2,prompt)
                       driver.find_element_by_xpath(u"//div/button[contains(text(),'确定')]").click()

               except NoSuchElementException:
                        pass
                        print "%s login successfully to %s"%(member,linklist2)
               time.sleep(100)




###########删除用户#######################################
def delUserMutiple():
        members = memberAll
        for member in members:
                DeleteUser(member)

###########登录和注销#######################################
# login("normal","https://192.168.25.71/pangolin/login.html")
# driver.find_element_by_xpath(u"//a[@title='注销']").click()
# time.sleep(3)
# login("manager","https://192.168.25.71/pangolin/login.html")
# driver.find_element_by_xpath(u"//a[@title='注销']").click()

#createUserMutiple()
#authUserMutilpe()
loginMultipleSubsystem()
#loginMultipleSoc()
driver.quit()
#delUserMutiple()