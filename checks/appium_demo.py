# coding=utf-8
"""
Created on 2018-05-22

@Filename: appium_demo
@Author: Gui


"""
# import unittest
# import os
# from appium import webdriver
#
# PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '8.0.0'
# desired_caps['deviceName'] = 'Android Emulator'
# desired_caps['app'] = PATH('appsearch_AndroidPhone_1012271b.apk')
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print(driver)
driver.find_element_by_xpath("//*[@text=1]").click()
driver.find_element_by_xpath("//*[@text=5]").click()
driver.find_element_by_xpath("//*[@text=6]").click()
driver.find_element_by_xpath("//*[@text=1]").click()
e = driver.find_element_by_id("com.android.calculator2:id/op_mul")
print(e)
e.click()
driver.quit()
