# -*- coding: UTF-8 -*-

# #调用模块封装
# from ls import ui
#
# driver = ui.openbrowser()
# driver.get('http://112.74.191.10:8000/')


#调用类封装

from ls.ui import Web

web = Web()

web.openbrowser()
web.driver.get('http://112.74.191.10:8000/')