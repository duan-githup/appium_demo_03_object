from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

class BaseAction:

    def __init__(self, driver):
        # 获取驱动对象
        self.driver = driver
        # 模拟手势操作
        self.touch_action = TouchAction(driver)

    def base_find_element(self, feature, timeout=20, poll=0.5):
        """
        根据特征，找元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        feature_by, feature_value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(feature_by, feature_value))
        return element

    def base_find_elements(self, feature, timeout=10, poll=1):
        """
        根据特征，找多个符合条件的元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        feature_by, feature_value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(feature_by, feature_value))
        return element

    def base_click(self, feature):
        """
        点击操作
        :param feature:
        :return:
        """
        el = self.base_find_element(feature)
        el.click()


    def base_input(self, feature, content):
        """
        输入并清空操作
        :param feature:
        :param content:
        :return:
        """
        el = self.base_find_element(feature)
        el.clear()
        el.send_keys(content)

    def base_clear(self, feature):
        """
        清空操作
        :param feature:
        :return:
        """
        self.base_find_element(feature).clear()


    def base_touch_press(self,el=None,x=None,y=None):
        """
        模拟手势按下松开
        :param feature:
        :return:
        """
        self.touch_action.press(el=el,x=x,y=y).release().perform()

    def base_slide_swipe(self,start_x,start_y,end_x,end_y,time):
        """
        滑动
        :param start_x:
        :param start_y:
        :param end_x:
        :param end_y:
        :param time:
        :return:
        """
        self.driver.swipe(start_x,start_y,end_x,end_y,time)


    def base_keycode(self,keycode):
        """
        模拟键盘操作
        :return:
        """
        self.driver.press_keycode(keycode)
        # self.driver.keyevent(keycode)