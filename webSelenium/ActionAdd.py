# -*- coding: utf-8 -*-
from functools import wraps
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

mailname = "mail001"
mailaddress = "shaojuan.wang@polydata.com.cn"
syslogname = "syslog000"
syslogipaddress = "192.168.24.106"
snmpname = "snmp000"
snmpipaddress = "192.168.24.106"



def newadd(func):
    @wraps(func)
    def loginadd(*arg):
        login(driver,user,base_url)
        time.sleep(5)
        yigou=driver.find_element_by_xpath(u"//span[contains(text(), '对象管理')]")
        ActionChains(driver).move_to_element(yigou).perform()
        driver.find_element_by_xpath("//a[@href='#/object/action']").click()
        time.sleep(3)
        driver.find_element_by_xpath(u"//span[contains(text(), '新增')]").click()
        time.sleep(3)
        print(func.__name__ + " was called")
        return func(*arg)
    return loginadd

@newadd
def ActionAddmail(mailname,mailaddress):
    driver.find_element_by_xpath(u"(//a[contains(text(),'邮件')])").click()
    driver.find_element_by_css_selector("div.form-group > #instancename").clear()
    driver.find_element_by_css_selector("div.form-group > #instancename").send_keys("%s" %(mailname))
    driver.find_element_by_id("reserved1").clear()
    driver.find_element_by_id("reserved1").send_keys("%s" %(mailaddress))
    Select(driver.find_element_by_xpath("//form[@id='groupForm']/div[2]/div[3]/div[2]/div/select")).select_by_visible_text(u"安全事件")
    driver.find_element_by_xpath("(//option[@value='2'])[3]").click()
    driver.find_element_by_id("description").clear()
    driver.find_element_by_id("description").send_keys("fffff")
    driver.find_element_by_xpath("//form[@id='groupForm']/div[3]/button[2]").click()
    #driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
    driver.find_element_by_xpath(u"//div/button[contains(text(), '提交')]").click()


@newadd
def ActionAddsyslog(syslogname,syslogipaddress):
    driver.find_element_by_link_text("Syslog").click()
    driver.find_element_by_css_selector("div.form-group > #instancename").clear()
    driver.find_element_by_css_selector("div.form-group > #instancename").send_keys("%s" %(syslogname))
    driver.find_element_by_id("reserved1").clear()
    driver.find_element_by_id("reserved1").send_keys("%s" %(syslogipaddress))
    driver.find_element_by_id("reserved2").clear()
    driver.find_element_by_id("reserved2").send_keys("514")
    Select(driver.find_element_by_xpath("//form[@id='groupForm']/div[2]/div[6]/div[2]/div/select")).select_by_visible_text(u"安全事件")
    driver.find_element_by_xpath("(//option[@value='2'])[3]").click()
    driver.find_element_by_id("description").click()
    #driver.find_element_by_xpath("//form[@id='groupForm']/div[3]/button[2]").click()
    #driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
    #driver.find_element_by_css_selector("#ToolTables_mytable1_0 > span").click()
    driver.find_element_by_xpath(u"//div/button[contains(text(), '提交')]").click()


@newadd
def ActionAddTrap(snmpname,snmpipaddress):
    driver.find_element_by_link_text("SNMP Trap").click()
    driver.find_element_by_css_selector("div.form-group > #instancename").clear()
    driver.find_element_by_css_selector("div.form-group > #instancename").send_keys("%s" %(snmpname))
    driver.find_element_by_id("reserved1").clear()
    driver.find_element_by_id("reserved1").send_keys("%s" %(snmpipaddress))
    driver.find_element_by_id("reserved2").clear()
    driver.find_element_by_id("reserved2").send_keys("162")
    Select(driver.find_element_by_xpath("//form[@id='groupForm']/div[2]/div[6]/div[2]/div/select")).select_by_visible_text(u"安全事件")
    driver.find_element_by_xpath("(//option[@value='2'])[3]").click()
    driver.find_element_by_id("description").click()
    #driver.find_element_by_xpath("//form[@id='groupForm']/div[3]/button[2]").click()
    #driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
    #driver.find_element_by_css_selector("#ToolTables_mytable1_0 > span").click()
    driver.find_element_by_xpath(u"//div/button[contains(text(), '提交')]").click()



ActionAddmail(mailname,mailaddress)
ActionAddsyslog(syslogname,syslogipaddress)
ActionAddTrap(snmpname,snmpipaddress)
driver.close()
#print(ActionAddTrap.__name__)

# ActionAddmail("mail11","shaojuan.wang@polydata.com.cn")
# ActionAddsyslog("Syslog11","192.168.24.106")
# ActionAddTrap("SNMPtrap11","192.168.24.106")