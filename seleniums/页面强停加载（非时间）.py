#js 执行停止加载(下面两个方法不生效，依然还会转圈圈，使用插件法/esc法)
import threading
import time

import win32api
import win32con
from selenium import webdriver
#get方法等注意异步使用，否则阻塞厉害的网页，会顺序等待
#window.open方法打开的页面才能使用window.stop等方法关闭，否则不生效

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


def thread_wait_stop(wait_sec=3):
    """
    针对selenium的get(url)时间过长阻塞情况的模拟esc，必须异步才可发挥效果，故这里使用线程尝试
    如果是脚本则不需要，其默认线程
    """
    print("等待{}秒".format(wait_sec))
    time.sleep(wait_sec)  # 等待来确保元素已经加载
    threading.Thread(MyLibrary().keybd_event(27))






driver = webdriver.Chrome()
t1=time.time()
# driver.get("https://cn.noxinfluencer.com/youtube/channel/UCbCmjCuTUZos6Inko4u57UQ")
# driver.execute_script("window.open('https://cn.noxinfluencer.com/youtube/channel/UCq-Fj5jknLsUf-MWSy4_brA')")
# print('正加载中')
#加载时间过长，想强停
# driver.execute_script("window.stop('https://cn.noxinfluencer.com/youtube/channel/UCq-Fj5jknLsUf-MWSy4_brA')")
# driver.execute_script("window.stop ? window.stop() : document.execCommand('Stop');")
# 都不行
#selenium键盘鼠标操作不生效（上局顺序阻塞，需异步）
# 使用win32api库
# MyLibrary().keybd_event(27)   #27代表esc(测试后发现，get方法顺序执行导致这句等加载完才执行，所以必须使用异步可生效，下方是线程实现esc停止加载；
# 而新的窗口tag（同一个driver）不会，可以立刻让这句生效，好像因为新窗口是线程异步)


def driver_get(url):
    res=driver.get(url)
    return res





print('开始停止加载控制')
poll=[]
print('开始可能阻塞的线程任务')
thread_get=threading.Thread(target=driver_get)  #必须是对象，所以新建个函数driver_get()再实例化，直接放driver.get(xxx)线程不生效
poll.append(thread_get)
for t in poll:
    t.start()
print('开始等待2s')
time.sleep(2)
print('执行esc')
#注意启动后不要动鼠标点击其他窗口
MyLibrary().keybd_event(27)  #前提保证当前窗口是chrome(后面可以加个保证当前键鼠操作的是chrome浏览器的补丁)
# thread_wait_stop()

# driver.execute_script("window.stop()")  #不生效是只能针对window.open()打开的窗口，https://www.likecs.com/show-305827478.html#sc=375
t2=time.time()

print('已执行停止加载')
print(t2-t1)
time.sleep(30)



