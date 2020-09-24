class Website:
    """网站注册"""


    def register(self, device, code):
        """发送验证信息"""
        device.send(code)


class Device:
    def send(self, code):
        print("发送信息")


class Phone(Device):
    """手机设备"""

    def send(self, code):
        """发送手机验证码"""
        print(f"发送手机验证码：{code}")


class Email(Device):
    """邮箱设备"""

    def send(self, code):
        """发送邮箱链接"""
        print(f'发送邮箱激活链接：http://www.baidu.com/{code}')


# 创建网站
baidu = Website()

# 创建两个不同设备
iphone11 = Phone()
email_163 = Email()

# 开始注册
baidu.register(iphone11, '123456')  # 发送手机验证码：123456
baidu.register(email_163, '123456')  # 发送邮箱激活链接：http://www.baidu.com/123456
