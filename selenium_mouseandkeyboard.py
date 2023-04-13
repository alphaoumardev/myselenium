# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/1/16 14:47
# @Author : firworkseasycold
# @Email : 1476094297@qq.com
# @File : selenium键盘.py
# @Software: PyCharm
#selenium自带
# send_keys(Keys.BACK_SPACE)：删除键(BackSpace)
# send_keys(Keys.SPACE)：空格键(Space)
# send_keys(Keys.TAB)：制表键(TAB)
# send_keys(Keys.ESCAPE)：回退键(ESCAPE)
# send_keys(Keys.ENTER)：回车键(ENTER)
# send_keys(Keys.CONTROL,‘a’)：全选(Ctrl+A)
# send_keys(Keys.CONTROL,‘c’)：复制(Ctrl+C)
# send_keys(Keys.CONTROL,‘x’)：剪切(Ctrl+X)
# send_keys(Keys.CONTROL,‘v’)：粘贴(Ctrl+V)
# send_keys(Keys.F1)：键盘F1

# 原文链接：https://blog.csdn.net/weixin_42636075/article/details/127103297
import time
import win32api
import win32con
import ctypes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver.get("https://cn.noxinfluencer.com/youtube/channel/UCq-Fj5jknLsUf-MWSy4_brA'")
driver.execute_script("window.open('https://cn.noxinfluencer.com/youtube/channel/UCq-Fj5jknLsUf-MWSy4_brA')")  #执行js脚本（发现不会像get阻塞导致强停失效，原因是异步）
time.sleep(2)
print('模拟按esc')
class MyLibrary(object):
    # VK_CODE为键盘编码
    def keybd_event(self,VK_CODE):
        """
        ESC键VK_ESCAPE (27)
        回车键：VK_RETURN (13)
        TAB键：VK_TAB (9)
        Caps Lock键：VK_CAPITAL (20)
        Shift键：VK_SHIFT (16)
        Ctrl键：VK_CONTROL (17)
        Alt键：VK_MENU (18)
        空格键：VK_SPACE (32)
        退格键：VK_BACK (8)
        左徽标键：VK_LWIN (91)
        右徽标键：VK_RWIN (92)
        鼠标右键快捷键：VK_APPS (93)
        Insert键：VK_INSERT (45)
        Home键：VK_HOME (36)
        Page Up：VK_PRIOR (33)
        PageDown：VK_NEXT (34)
        End键：VK_END (35)
        Delete键：VK_DELETE (46)
        方向键(←)：VK_LEFT (37)
        方向键(↑)：VK_UP (38)
        方向键(→)：VK_RIGHT (39)
        方向键(↓)：VK_DOWN (40)
        F1键：VK_F1 (112)
        F2键：VK_F2 (113)
        F3键：VK_F3 (114)
        F4键：VK_F4 (115)
        F5键：VK_F5 (116)
        F6键：VK_F6 (117)
        F7键：VK_F7 (118)
        F8键：VK_F8 (119)
        F9键：VK_F9 (120)
        F10键：VK_F10 (121)
        F11键：VK_F11 (122)
        F12键：VK_F12 (123)
        Num Lock键：VK_NUMLOCK (144)
        小键盘0：VK_NUMPAD0 (96)
        小键盘1：VK_NUMPAD1 (97)
        小键盘2：VK_NUMPAD2 (98)
        小键盘3：VK_NUMPAD3 (99)
        小键盘4：VK_NUMPAD4 (100)
        小键盘5：VK_NUMPAD5 (101)
        小键盘6：VK_NUMPAD6 (102)
        小键盘7：VK_NUMPAD7 (103)
        小键盘8：VK_NUMPAD8 (104)
        小键盘9：VK_NUMPAD9 (105)
        小键盘。：VK_DECIMAL (110)
        小键盘*：VK_MULTIPLY (106)
        小键盘+：VK_ADD (107)
        小键盘-：VK_SUBTRACT (109)
        小键盘/：VK_DIVIDE (111)
        Pause Break键：VK_PAUSE (19)
        Scroll Lock键：VK_SCROLL (145)

        """
        # @Keyboard
        # input
        VK_CODE = int(VK_CODE)
        print(":::VK_CODE:", VK_CODE)
        win32api.keybd_event(VK_CODE, 0, 0, 0)
        win32api.keybd_event(VK_CODE, 0, win32con.KEYEVENTF_KEYUP, 0)
        print(":::press", str(VK_CODE), "successfully!")
        time.sleep(2)


# webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()  #想用于停止加载但不生效，不能手动直接停止，据说只能关闭弹窗，待测
MyLibrary().keybd_event(27)  #有效果，感谢http://t.csdn.cn/PRpQr；#有效果，但是针对页面加载阻塞，需要异步才可
print('结束')

while True:
    b=input()
    if b=='b':
        break