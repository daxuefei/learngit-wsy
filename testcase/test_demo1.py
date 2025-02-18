from selenium import webdriver
import time
class TestDemo:
    def test_demo1(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com")
        time.sleep(5)
        driver.quit()
        print("test1,打开浏览器")


