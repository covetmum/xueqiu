# -*- encoding：utf-8 -*-
# @Time:2022/4/11 3:44 下午
# @Auto:guohuashang
# @FileName:searchpage.py
# @Emial:
# @Function:
import time
import pytest
from page.Basepage import Basepage
from appium.webdriver.common.mobileby import MobileBy

class searchpage(Basepage):
    def search(self,revtext=None):
        self.find(MobileBy.ID,"search_input_text").send_keys(revtext)
        self.find(MobileBy.ID,"name").click()
        time.sleep(3)
        return self
    def get_price(self):

        return float(self.find(MobileBy.ID,"current_price").text)

