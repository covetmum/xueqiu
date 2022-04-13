# -*- encoding：utf-8 -*-
# @Time:2022/4/7 5:28 下午
# @Auto:guohuashang
# @FileName:StartApp.py
# @Emial:
# @Function:
import sys
import time

from appium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy as By
# from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
import os

appPackage="com.xueqiu.android"
appActivity=".view.WelcomeActivityAlias"
caps={
  "platformName": "Android",
  'automationName':"UiAutomator2",
  "platformVersion": "7.1.2",
  "deviceName": "127.0.0.1:62001",
  "noReset": True,
  # "chromedriverExecutable":"/Users/yenuo/PycharmProjects/xueqiu/chromedriver"
  "appium:appPackage": appPackage,
  "appium:appActivity": appActivity
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
time.sleep(2)

# os.system("adb shell input keyevent 3")
time.sleep(2)
#启动app函数
# driver.launch_app()
# driver.start_activity(appPackage,appActivity)
# 切换进入H5页面
# driver.switch_to.context('com.xueqiu.android')
# #退出H5页面
# driver.switch_to.default_content()

# w=driver.get_window_size()['width']
# h=driver.get_window_size()['height']
# "adb shell input swipe x1 y1 x2 y2 time"
# driver.swipe(888,800,111,800,1000)
# "adb shell input tap x1 y1"
# driver.tap([(100,100)])
# driver.keyevent(3)
TouchAction(driver).move_to(ele,x,y).wait().perform()


# driver.implicitly_wait(10)
# driver.find_element(By.ID,"com.xueqiu.android:id/profile_image").click()
# driver.find_element(By.CSS_SELECTOR,"*[text='手机号']").click()
# # driver.find_element(By.ANDROID_UIAUTOMATOR,"new UiSelector().text('手机号')").click()
# # driver.find_element(By.ACCESSIBILITY_ID,'content-desc属性值')
# driver.find_element(By.ID,"com.xueqiu.android:id/register_phone_number").send_keys("13526662456")
# driver.find_element(By.ID,"com.xueqiu.android:id/register_code").send_keys("1234")
# driver.find_element(By.ID,"com.xueqiu.android:id/button_next").click()

# toast_message='请先勾选并同意相关协议'
# message=f"//*[@text={toast_message}]"
# message="//*[contains(@text,'请先勾选并同意相关协议')]"
# toast=driver.find_element(By.XPATH,message)
# toast=WebDriverWait(driver,10).until(lambda x:x.find_element(By.XPATH,message))
# toast=WebDriverWait(driver,10).until(driver.find_element(By.XPATH,message))
# print(toast.text)
