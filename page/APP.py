# -*- encoding：utf-8 -*-
# @Time:2022/4/11 2:41 下午
# @Auto:guohuashang
# @FileName:APP.py
# @Emial:
# @Function:
import os

from appium import webdriver
from page.Basepage import Basepage
from page.Main import Main
class APP(Basepage):
    __host="127.0.0.1"
    __port=4723
    # __Version=os.system("adb shell getprop ro.build.version.release")
    __Version="7.1.2"
    __deviceName="127.0.0.1:62001"
    __noReset=True
    __appPackage='com.xueqiu.android'
    __appActivity=".view.WelcomeActivityAlias"
    def start(self):
        if self.driver is None:
            caps = {}
            caps['platformName'] = "Android"
            caps['platformVersion'] = self.__Version
            caps['deviceName'] = self.__deviceName
            caps['noReset'] = self.__noReset
            caps['unicodeKeyboard'] = True
            caps['resetKeyboard'] = True
            caps['appPackage'] = self.__appPackage
            caps['appActivity'] = self.__appActivity
            appium_driver = f"http://{self.__host}:{self.__port}/wd/hub"
            self.driver = webdriver.Remote(appium_driver, caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.start_activity(self.__appPackage,self.__appActivity)
            self.driver.implicitly_wait(10)
        return self
    def main(self):
        return Main(self.driver)