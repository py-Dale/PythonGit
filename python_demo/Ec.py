from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

'''方法大全参考 https://zhuanlan.zhihu.com/p/41567159'''
# 封装 WebDriverWait 显示等待+EC 方法
class WebWait():
    def __init__(self,driver:webdriver):
        self.driver = driver

    '''判断对象加到了dom树里，若存在则返回该元素element，无需元素可见即可'''
    def presence_of_element_located(self,locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element
    '''判断对象是否被添加到了dom里并且可见，返回该元素 element'''
    def visibility_of_element_located(self,locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
        return element
    '''判断元素是否可见，如果可见就返回这个元素 传入str不带括号'''    
    def visibility_of(self,locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of(self.driver.find_element(locator)))
        return element
    '''判断是否至少有1个对象存在于dom树中，如果定位到就返回列表'''
    def presence_of_all_elements_located(self,locator):
        element_list = WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(locator))
        return element_list
    '''判断至少有一个对象在页面可见，如果存在则返回列表'''
    def visibility_of_any_elements_located(self,locator):
        element_list = WebDriverWait(self.driver,10).until(EC.visibility_of_any_elements_located(locator))
        return element_list
    '''判断指定的对象中是否包含了预期的字符串，返回布尔值 text 预期字符'''
    def text_to_be_present_in_element(self,locator,text):
        boolean = WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element(locator,text))
        return boolean
    '''判断对象的属性值中是否包含了预期的字符串，返回布尔值'''
    '''包含value属性的html标签：<button> <input> <li> <meter> <option><progress> 且是有values值'''
    def text_to_be_present_in_element_value(self,locator,text):
        boolean = WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element_value(locator,text))
        return boolean
    '''判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False'''
    '''driver.switchTo() 可直接进入'''
    def frame_to_be_available_and_switch_to_it(self,frame):
        element = WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it(frame))
        return element
    '''判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回True  注意swfEveryCookieWrap在此页面中是一个隐藏的元素 display=none'''
    def invisibility_of_element_located(self,locator):
        boolean = WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(locator))
        return boolean   
    '''判断某个元素中是否可见并且是enable的，代表可点击,可点击则执行点击，否则返回None，不会报错'''
    def element_to_be_clickable(self,locator):
        element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locator)).click()
        if element:
            element.click()
        else:
            return False 
    '''等待某个元素从dom树中移除 注意括号'''
    def staleness_of(self,locator):
        element = WebDriverWait(self.driver,10).until(EC.staleness_of(self.driver.find_element(locator)))
        return element 
    '''判断对象是否被选择，一般用于下拉列表。被选择返回True，否则返回False'''
    '''位置的写法'''
    def element_located_to_be_selected(self,locator):
        boolean = WebDriverWait(self.driver,2).until(EC.element_located_to_be_selected(locator),None)
        return boolean 
    '''元素的写法'''
    def element_to_be_selected(self,locator):
        boolean = WebDriverWait(self.driver,2).until(EC.element_to_be_selected(self.find_element(locator)),None)
        return boolean 
    '''判断某个元素选中状态是否与预期一致，一致返回True，否则返回False'''
    '''元素的写法'''
    def element_selection_state_to_be(self,locator):
        boolean = WebDriverWait(self.driver,3).until(EC.element_selection_state_to_be(self.driver.find_element(locator)),True)
        return boolean 
    '''位置的写法'''
    def element_located_selection_state_to_be(self,locator):
        boolean = WebDriverWait(self.driver,3).until(EC.element_located_selection_state_to_be(locator),True)
        return boolean 
    '''判断按钮是否被选中'''
    def selected(self,locator):
        boolean = self.driver.find_element(locator).is_selected()
        return boolean
    '''判断网页句柄个数 返回布尔值 count 数量int'''
    def number_of_windows_to_be(self,count):
        boolean = WebDriverWait(self.driver,10).until(EC.number_of_windows_to_be(count))
        return boolean 
    '''alert_is_present判断是否有告警页面，如果有跳转至告警页面，否则返回False,有则点击接受'''
    def alert_is_present(self):
        element = WebDriverWait(self.driver,2).until(EC.alert_is_present())
        if element:
            element.accept()
        else:
            return False


'''把显示等待和判断封装成方法取调用，代码简洁明了'''
# driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# driver.get("https://www.baidu.com/")
# loasd = (By.ID,'s-usersetting-top')
# WebWait(driver).presence_of_element_located(loasd).click()