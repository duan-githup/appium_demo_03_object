from base.base_driver import GetDriver
from page.pages import Page
import pytest
from base.base_yaml import loads


class TestLogin:

    # @classmethod
    # def setup_class(cls):
    #     cls.driver = GetDriver.init_driver()
    #     cls.p = Page(cls.driver)
    #
    # @classmethod
    # def teardown_class(cls):
    #     cls.driver.quit()


    def setup(self):
        self.driver = GetDriver.init_driver()
        self.p = Page(self.driver)
        print("开始")

    def teardown(self):
        GetDriver.qiut_driver(self.driver)
        print("结束")

    @pytest.mark.parametrize("data",loads("login_data","login_case"))
    def test_login(self,data):
        self.p.login().p_execute(data["name"],data["pwd"],data["code"])

