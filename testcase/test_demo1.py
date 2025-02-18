import pytest
from selenium import webdriver

class TestDemo():
    def test_demo1(self):
        browser=webdriver.Chrome()
        browser.set_page_load_timeout(10)
        browser.get("https://www.baidu.com")
        print("tsst1,打开百度页面")


    def test_demo2(self):
        print("tsst2")

if __name__=="__main__":
    pytest.main()