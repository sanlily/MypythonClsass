# -*- coding: UTF-8 -*-



# 调用谷歌浏览器 绝对路径
#driver = webdriver.Chrome(executable_path='I:\driverls\chromedriver')

# 打开百度
#driver.get('https://www.baidu.com')

#退出浏览器
#driver.quit()

# 打开练习地址
# driver.get('http://112.74.191.10:8000/')


from selenium import webdriver
import os, traceback



# # 定义一个函数，用来打开浏览器
# def openbrowser():
#     # 创建一个ChromeOptions的对象
#     option = webdriver.ChromeOptions()
#
#     #去掉浏览器提示条配置
#     option.add_argument('disable-infobars')
#
#     # 获取用户目录，解决加载慢的问题
#     try:
#         #异常处理，如果获取到，就使用获取到的路径
#         userdir = os.environ['USERPROFILE']
#     except Exception as e:
#         #如果没有获取到，就使用默认的Adminstrator路径
#         #打印异常信息
#         traceback.print_exc()
#         userdir = 'C:\\Users\\Adminstrator'
#
#     userdir += '\\AppData\\Local\\Google\\Chrome\\User Data'
#     userdir = 'user-data-dir=' + userdir
#     #print(userdir)
#
#     #添加用户目录
#     option.add_argument(userdir)
#
#     # 调用谷歌浏览器 相对路径
#     driver = webdriver.Chrome(executable_path='../lib/chromedriver',options = option)
#     return driver


# 浏览去掉浏览器提示条配置地址
#driver.get('http://112.74.191.10:8000/')



# 定义一个class，用来打开浏览器

class Web:
    def __int__(self):
        # 初始化浏览器的实例变量
        self.drever = None

      #定义函数，专门用来打开浏览器
    def openbrowser(self):
        # 创建一个ChromeOptions的对象
        option = webdriver.ChromeOptions()

        #去掉浏览器提示条配置
        option.add_argument('disable-infobars')

        # 获取用户目录，解决加载慢的问题
        try:
            #异常处理，如果获取到，就使用获取到的路径
            userdir = os.environ['USERPROFILE']
        except Exception as e:
            #如果没有获取到，就使用默认的Adminstrator路径
            #打印异常信息
            traceback.print_exc()
            userdir = 'C:\\Users\\Adminstrator'

        userdir += '\\AppData\\Local\\Google\\Chrome\\User Data'
        userdir = 'user-data-dir=' + userdir
        #print(userdir)

        #添加用户目录
        option.add_argument(userdir)

        # 调用谷歌浏览器 相对路径
        self.driver = webdriver.Chrome(executable_path='../lib/chromedriver',options = option)
        return self.driver
