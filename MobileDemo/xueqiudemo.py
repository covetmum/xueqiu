# -*- encoding：utf-8 -*-
# @Time:2022/4/8 4:35 下午
# @Auto:guohuashang
# @FileName:xueqiudemo.py
# @Emial:
# @Function:
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
caps={}
caps['platformName']="Android"
caps['platformVersion']="7.1.2"
caps['deviceName']="127.0.0.1:62001"
caps['noReset']=True
caps['unicodeKeyboard']=True
caps['resetKeyboard']=True
caps['appPackage']='com.xueqiu.android'
caps['appActivity']='.view.WelcomeActivityAlias'
appium_driver="http://127.0.0.1:4723/wd/hub"
driver=webdriver.Remote(appium_driver,caps)

driver.implicitly_wait(20)
driver.find_element(MobileBy.XPATH,"//*[@text='股票' and @resource-id=\"com.xueqiu.android:id/tab_name\"]").click()
driver.find_element(MobileBy.ID,"action_search").click()
driver.find_element(MobileBy.ID,"search_input_text").send_keys("alibaba")
driver.find_element(MobileBy.ID,"name").click()



