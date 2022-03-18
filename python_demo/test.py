from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Ec


class test_Ec():
    
    def __init__(self, driver):
        self.driver = driver
    
    def test(self):
        # 访问网址
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        loasd = (By.ID,'s-usersetting-top')
        Ec.WebWait(self.driver).presence_of_element_located(loasd).click()


driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
a = test_Ec(driver).test()

