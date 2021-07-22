
from appium import webdriver

class GetDriver:

    driver = None

    @classmethod
    def init_driver(cls):

        if cls.driver is None:

            desired_caps = dict()
            # 设备信息
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '9'
            desired_caps['deviceName'] = 'V89LCIAMNFKRAQBM'
            # app信息
            desired_caps['appPackage'] = 'com.ane.scb'
            desired_caps['appActivity'] = '.ui.page.LoginActivity'

            desired_caps['automationName'] = 'Uiautomator1'

            # 隐藏键盘
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True

            cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        return cls.driver

    @classmethod
    def qiut_driver(cls,driver):
        """
        关闭对象必须清空为 None
        :param driver:
        :return:
        """
        driver.quit()
        cls.driver = None


if __name__ == '__main__':
    GetDriver.init_driver()


