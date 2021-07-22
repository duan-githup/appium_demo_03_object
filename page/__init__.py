from selenium.webdriver.common.by import By

# 服务器地址
login_server_IP = "192.168.3.244"

# 输入服务器IP地址
login_server = By.ID,"com.ane.scb:id/et_dialog_content"
# 点击确定
login_confirm = By.XPATH,"//*[@text='确定']"
# 输入用户名
login_userName = By.XPATH,"//*[@text='请输入账号']"
# 输入登录密码
login_password = By.XPATH,"//*[@text='请输入登录密码']"
# 输入验证码
login_code = By.XPATH,"//*[@text='验证码']"