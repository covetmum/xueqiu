# -*- encoding：utf-8 -*-
# @Time:2022/4/11 3:39 下午
# @Auto:guohuashang
# @FileName:Main.py
# @Emial:
# @Function:
import time
from appium.webdriver.common.mobileby import MobileBy
from page.Basepage import Basepage
from page.searchpage import searchpage
from page.mypage import mypage
class Main(Basepage):
    def go_to_searchpage(self):
        # value="//*[@id='home_search']/android.widget.RelativeLayout/android.widget.ViewFlipper/android.widget.LinearLayout/android.widget.TextView"
        value="//*/android.widget.ViewFlipper/android.widget.LinearLayout/android.widget.TextView"
        self.find(MobileBy.XPATH,value).click()
        time.sleep(3)
        return searchpage(self.driver)
    def go_to_mypage(self):
        value=""
        self.find(MobileBy.XPATH,value).click()
        return mypage(self.driver)