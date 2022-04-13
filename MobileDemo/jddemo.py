# -*- encoding：utf-8 -*-
# @Time:2022/4/8 11:55 上午
# @Auto:guohuashang
# @FileName:jddemo.py
# @Emial:
# @Function:
import time

from appium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy as By
caps={
  "appium:platformName": "Android",
  'appium:automationName':"UiAutomator2",
  "appium:platformVersion": "7.1.2",
  "appium:deviceName": "127.0.0.1:62001",
  "appium:noReset": True,
  "appium:appPackage": "com.jingdong.app.mall",
  "appium:appActivity": ".main.MainActivity"
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
driver.implicitly_wait(20)
driver.find_element(By.XPATH,"//android.view.View[@content-desc=\"我的\"]").click()
driver.find_element(By.ID,"com.jd.lib.personal.feature:id/jh").click()
# driver.find_element(By.ANDROID_UIAUTOMATOR,"new UiSelector().text('手机号')").click()
# driver.find_element(By.ACCESSIBILITY_ID,'content-desc属性值')
driver.find_element(By.ID,"com.xueqiu.android:id/register_phone_number").send_keys("13526662456")
driver.find_element(By.ID,"com.xueqiu.android:id/register_code").send_keys("1234")
driver.find_element(By.ID,"com.xueqiu.android:id/button_next").click()
time.sleep(1)