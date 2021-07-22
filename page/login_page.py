from base.base_action import BaseAction
import allure,page as p

from base.base_driver import GetDriver
from base.base_log import GetLogging

log = GetLogging.get_log()


class LoginPage(BaseAction):

    @allure.step("设置服务器IP地址")
    def p_setting_server(self,x=208,y=1641):
        log.success("点击设置服务器按钮")
        self.base_touch_press(x=x,y=y)


    @allure.step("输入服务器IP地址")
    def p_input_server(self):
        log.success("输入服务器IP地址")
        self.base_input(p.login_server,p.login_server_IP)


    @allure.step("确定")
    def p_qued_server(self):
        log.success("点击确定按钮")
        self.base_click(p.login_confirm)


    @allure.step("输入登录用户名")
    def p_userName(self,userName):
        log.success("输入用户名")
        self.base_input(p.login_userName,userName)


    @allure.step("输入登录密码")
    def p_password(self,pwd):
        log.success("输入用户密码")
        self.base_input(p.login_password,pwd)


    @allure.step("输入验证码")
    def p_code(self,code):
        log.success("输入验证码")
        self.base_input(p.login_code,code)


    @allure.step("登录")
    def p_submit(self,x=739,y=1626):
        log.success("点击登录")
        self.base_touch_press(x=x,y=y)


    @allure.step("执行")
    def p_execute(self,userName,pwd,code):
        self.p_setting_server()
        self.p_input_server()
        self.p_qued_server()
        self.p_userName(userName)
        self.p_password(pwd)
        self.p_code(code)
        self.p_submit()

if __name__ == '__main__':
    from time import sleep

    driver = GetDriver().init_driver()
    try:
        LoginPage(driver).p_execute("admin","123456","TEST")
        sleep(5)
    except Exception as e:
        print(e)
    driver.quit()
