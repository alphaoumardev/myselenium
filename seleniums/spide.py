
import csv
import time

import pymysql
# import win32api
# import win32con
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# from scripts.python模拟键盘鼠标操作 import MyLibrary

vpnuser="alphaoumardev@outlook.com"
pwd='bonjouroumar200'  #也是邮箱密码 /usr/local/bin/chromedriver

all_user_pool=[
    #用一个扔一个
    # {"13451728020@163.com":"81762371lbj123"}, #已废弃
    {"suzhaoli9909@gmail.com":"81762371lbj123"},
    {"sleepshark@0219@gmail.com":"81762371lbj123"},
    {"15321398040@163.com":"81762371lbj123"},
]



# sleepshark@0219@gmail.com 81732371lbj123
# sleepshark@0219@gmail.com
# sleepshark@0219@gmail.com
# sleepshark@0219@gmail.com
# sleepshark@0219@gmail.com

class MyLibrary(object):
    """
    python模拟键盘鼠标操作
    """
    # VK_CODE为键盘编码
    @staticmethod
    def keybd_event(VK_CODE):
        # @Keyboard
        # input
        VK_CODE = int(VK_CODE)
        print(":::VK_CODE:", VK_CODE)
        # win32api.keybd_event(VK_CODE, 0, 0, 0)
        # win32api.keybd_event(VK_CODE, 0, win32con.KEYEVENTF_KEYUP, 0)
        print(":::press", str(VK_CODE), "successfully!")
        time.sleep(2)


def choose_user(user_index=0):
    global user_login, pwd_login
    for k,v in all_user_pool[user_index].items():
        user_login,pwd_login=k,v
    return user_index,user_login,pwd_login
#后续user池选择

print('尝试打开chrome')


#nox登录的url
nox_login_brand="https://cn.noxinfluencer.com/login?userType=brand&service=https%3A%2F%2Fcn.noxinfluencer.com%2F"

def check_ban():
    """
    nox校验被ban
    div
    bs4写法，待使用
    """
    # ban_str = '<div class="content confirm">'
    # soup = BeautifulSoup(html, 'html5lib')  # 返回匹配出的所有class名为xxx的div值
    # if soup.select("div[class='content confirm']"):  # 不为空则说明被ban
    #     print('time.time()，被办，请更换信息')
    try:
        driver.find_element(By.CSS_SELECTOR,'div[class="content confirm"]')  #地址被ban
        driver.find_element(By.CSS_SELECTOR, 'p[class="des"]')  #访问量被ban
        error_tips = {'1000': '已被反爬办了'}
        return error_tips
    except NoSuchElementException:
        success_tips={'999':'get访问成功,未被ban'}
        return success_tips


def driver_get(url):
    """如果需要用封装好用于thread"""
    return driver.get(url)


def start_driver(executable_path=r"/usr/local/bin/chromedriver"):
    print('初始化--driver')
    try:
        # if tag=='Firefox':
        #     options = webdriver.FirefoxOptions()
        #     driver=webdriver.Firefox(executable_path=r"/usr/local/bin/chromedriver")
        # elif tag=='Edge':
        #     options = webdriver.EdgeOptions()
        #     driver=webdriver.Edge(executable_path)
        # elif tag=='Ie':
        #     options = webdriver.IeOptions()
        #     driver=webdriver.Ie(executable_path)
        # else:
            #默认chrome
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path)
        # # 设定页面加载timeout时长，需要的元素能加载出来就行
        # driver.set_page_load_timeout(15)
        # driver.set_script_timeout(15)
        return options,driver
    except Exception as e:
        print('浏览器驱动启动失败:',e)





def nox_login(url=nox_login_brand,user_login='',pwd_login=''):
    """默认品牌方"""
    if url==nox_login_brand:
        driver.get(url) #会导致阻塞，需要异步或者线程来强停,否则会等待加载再继续
        # thread_get = threading.Thread(target=driver_get,args=url)  # 必须是对象，所以新建个函数driver_get()再实例化，直接放driver.get(xxx)线程不生效
        # thread_get.start()  #实际使用线程保持，待解决
        time.sleep(12)
        # frist_handle = driver.current_window_handle  #获取当前窗口句柄
        # driver.switch_to.window(frist_handle)  #跳转到此句柄窗口

      #模拟esc按键手动停止加载防止加载过长),线程是因为get过长阻塞导致,需要异步来停止加载，实际多执行几次强停可以不异步达到去除阻塞导致的卡住效果
        user_id = "email"  # 具体的或者re表达式
        pwd_id = "pwd"
        # pwd_id_text = "pwd-text"  #两个input输入框嵌套
        submit_id = "login-submit"

        print('开始登录')

        try:
            user_dw=driver.find_element("id", value=user_id)  #返回element对象
            user_dw.click()  # 点击，可省略
            user_dw.clear()  # 清空输入，可省略
            user_dw.send_keys(user_login)  # 在输入框输入
            # value_user = user_dw.get_attribute('value')  # .text方法拿不到input的值，用这个查看,具体搜索get_attribute用法
        except Exception as e:
            error_tips={'1002','登录用户名定位失败'}
            print(error_tips,e)
            return error_tips

        try:
            pwd_dw = driver.find_element("id", value=pwd_id)
            pwd_dw.click()
            pwd_dw.send_keys(pwd_login)
        except Exception as e:
            error_tips={'1003','密码输入失败'}
            print(error_tips, e)
            return error_tips

        try:
            subbutton_dw = driver.find_element(by=By.ID, value=submit_id)
            subbutton_dw.click()
        except Exception as e:
            error_tips = {'1004','登录操作失败'}
            print(error_tips,e)
            return error_tips


        time.sleep(9)  #必须等待，否则会导致不生效
        # 模拟按下esc
        MyLibrary().keybd_event(27)
        MyLibrary().keybd_event(27)
        MyLibrary().keybd_event(27)  #多加几个防止不生效

        #检查是否被ban
        print('登录成功')


        # 打开新窗口
        # driver.execute_script("window.open('https://cn.noxinfluencer.com/youtube/channel/UCq-Fj5jknLsUf-MWSy4_brA')") #只有script的opend才可stop
        # 如果开始get方法跳转页面会自动加载列表页，而且很长会卡住加载
        # driver.close()  # 关闭当前
        # return cookies
    else:
        print('网红方登录待开发')


def list_input():
    driver.find_element(By.CSS_SELECTOR,"")


#设置代理在options里add

# def check_element_exists(xpath):
#     """检查是否存在元素"""
#     try:
#         driver.find_element(xpath)
#     except NoSuchElementException:
#         return False
#     return True



def get_html():
    """获取页面源码以及当前url"""
    html_str = driver.page_source
    url=driver.current_url
    print(url)
    return html_str,url






def save_csv(path='',data_row=''):
    """根据情况，默认选择存储"""
    #G:\cyspider\webspider\spyder_web\nox\data\create_noxwh.csv
    with open(r''.format(path), 'a+', newline="",
              encoding='utf-8') as f:
        writer = csv.writer(f)
    writer.writerow(data_row) #dta_row为列表或元组类型，也可为单个str





class MysqlSpider(object):

    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.password = 'Bonjouroumar200@'
        self.db = 'nox'
        self.charset = 'utf8mb4'

    def connect(self,db):
        connection=pymysql.connect(host=self.host,
                        port=self.port,
                        user=self.user,
                        password=self.password,
                        charset=self.charset,
                        db=db
                        )
        return connection

    def act(self,action,db,more_sql='',data=''):
        connection=self.connect(self.db)
        with connection.cursor() as cur:
            if more_sql:
                my_sql_script = more_sql
            else:
                if action=='c':  #create
                    my_sql_script= "insert into {} values {}".format(db,data)
                elif action=='d':  #delete
                    my_sql_script = "delete from {} where ;".format(db,data)
                elif action=='u':  #update
                    my_sql_script=""
                else: #retrieve
                    my_sql_script = "select * from {};".format(db)
            #执行
            cur.execute(my_sql_script)




if __name__ == '__main__':
    #检查并链接数据库
    print('初始化-链接数据库')
    c = MysqlSpider()
    connection = c.connect('nox')
    # 读取索引
    sql = 'select * from `nox_wh_index`'
    try:
        with connection.cursor() as cur:
            cur.execute(sql)
            index_data=cur.fetchall()
    except Exception as e:
        print("获取索引失败，请停止程序并检查")
    wh_list_index, wh_index = index_data[0][0],index_data[0][1]
    # wh_list_index = 1  # 这里先手动修改，后面添加存储功能，实现自动更新
    print('当前列表页索引：{}，当前详情页索引：{}'.format(wh_list_index,wh_index))
    #1.启动浏览器
    options,driver=start_driver()
    while True:
        #2.选取登录用户
        user_index,user_login,pwd_login=choose_user(user_index=0)

        #3.登录  以及登录初始的判断 循环user_index+=1
        nox_login(user_login=user_login,pwd_login=pwd_login)

        #判断是否被ban
        result_tip=check_ban()
        if list(result_tip.keys())[0]=='1000':
            user_index+=1
            #重新登录
            break

        MyLibrary().keybd_event(27)
        MyLibrary().keybd_event(27)
        MyLibrary().keybd_event(27)

        # 网红列表页
        print('开始尝试访问列表页')
        #如果登录后很快就到这句print('开始访问列表页')，且之后迟迟没响应，可能是ip被ban了，需要换ip解决
        #上面情况，长时间不点击有大概率出现，点击后会概率下降 怀疑是有页面点击次数，没有点击的认为是爬虫，从而反爬不响应
        #但是经过实验意外发现
            # 1.通过控制页面前进后退可以有限解决，
            # 最好鼠标侧键法但不知道如何模拟按鼠标侧面的键，而driver控件前进后退有概率不行，比较坑)
            # 2.执行点击法 -点击设置的帮助链接等会有效果，多尝试，找找有几个有效果的
            #3.换了ip即可
        #下方发现，会在执行下面的三局点击法语句前阻塞，通过多个esc法解决了，但还是会有短暂等待
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[6]/span/span[2]').click()
        time.sleep(1) #等待1s来让下方加载
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[6]/div/div/div[7]/a/span').click()
        MyLibrary().keybd_event(27)


        # # 前进
        time1=time.time()

        print('正在访问列表页')
        #列表页——网红主页url获取
        try:
            wh_1='https://cn.noxinfluencer.com/brand/kolRecommend'  #此页面默认youtube
            driver.get(wh_1)

        except TimeoutError as e:
            # 超过500s,就是ip被ban换ip
            print('此ip可能被ban,或者尝试前进后退')
            break

        time.sleep(10)
        time2 = time.time()
        print(time2-time1)
        MyLibrary().keybd_event(27)
        MyLibrary().keybd_event(27)

        print('访问列表页成功')

        # #根据记录的列表页索并判断是否需要点击列表切换
        # if wh_list_index!=1:
        #     try:
        #         index_dw=driver.find_element(By.XPATH, "/html/body/section/section/div/div[2]/div/div[2]/div/ul/li[10]/div[2]/input")
        #     except ZeroDivisionError:
        #         #等待加载出
        #         time.sleep(5)
        #     index_dw.click()
        #     index_dw.clear()
        #     # sy = index_dw.text
        #     # print('sy:', sy)
        #     index_dw.send_keys(wh_list_index)  #注意下次循环之前需要清空这个输入框，否则会变成很大的数字
        #     time.sleep(5)

        while True:
            # 执行输入下一页动作来刷新列表
            # < div class ="ant-pagination-options-quick-jumper" > 跳至 < input type="text" > 页 < / div >
            time.sleep(15)
            try:
                index_dw = driver.find_element(By.XPATH,
                                               "/html/body/section/section/div/div[2]/div/div[2]/div/ul/li[10]/div[2]/input")
            except Exception as e:
                print(e)
                # 等待加载出
                time.sleep(5)
            index_dw.click()
            index_dw.clear()
            # sy = index_dw.text
            # print('sy:', sy)
            if wh_list_index==1:
                pass
            else:
                index_dw.click()
                index_dw.clear()
                index_dw.send_keys(wh_list_index)  # 注意下次循环之前需要清空这个输入框，否则会变成很大的数字
                index_dw.click()
                index_dw.clear()
                index_dw.send_keys(wh_list_index)  #执行两次防止不生效
            # 等待新的列表页加载完成
            time.sleep(10)

            #定位
            whlist_dw_list=driver.find_elements(By.CSS_SELECTOR,'tr[class="ant-table-row ant-table-row-level-0"]')
            # print(len(whlist_dw_list))
            #解析
            i=0
            for whlist_dw in whlist_dw_list:
                i+=1
                wh_nox_url = whlist_dw.get_attribute('data-row-key')  # nox网红的具体url  同youtube 为UCq-Fj5jknLsUf-MWSy4_brA
                # https://cn.noxinfluencer.com/youtube/channel/UCq-Fj5jknLsUf-MWSy4_brA
                whliststr=whlist_dw.text
                whliststr_list=whliststr.split('\n')
                sql = "insert into `nox_wh`(`whname`,`fansnum`,`language`,`tags`,`youtube`) values('{}','{}','{}','{}','{}');".format(
                    whliststr_list[0], whliststr_list[1], whliststr_list[3], whliststr_list[4],wh_nox_url)
                #values没有''会是insert into `nox_wh`(`whname`,`fansnum`,`country`,`tags`,`noxurl`) values(T-Series,235M,英语,娱乐 音乐 电视节目 电影,UCq-Fj5jknLsUf-MWSy4_brA);,也不能是``
                print(sql)
                # print(wh_nox_url)
                # print(whliststr)
                #存储
                # print('存储')
                try:
                    with connection.cursor() as cur:
                        cur.execute(sql) #保险起见，不使用批量，而是一条条
                        connection.commit()  # 如果数据库连接未配置为autocommit，则需要提交语句没有这个不会生效
                except Exception as e:
                    print('当前页第{}条失败'.format(i))
                    print(e)
                # print('下一个')
            # with open(r'G:\cyspider\webspider\spyder_web\nox\data\create_noxwh.csv','a+',newline="",encoding='utf-8') as f:  #newline=""保证不出现换行的空行
            #     writer= csv.writer(f)
            #     for whlist_dw in whlist_dw_list:
            #         wh_nox_url=whlist_dw.get_attribute('data-row-key')  #nox网红的具体url  例如UCq-Fj5jknLsUf-MWSy4_brA
            #         whlist_dw_text=whlist_dw.text
            #         data_row=whlist_dw_text #具体的值name,youtube粉丝，nox评分,语言/country,tags,
            #         print(data_row)
                    # """
                    # T-Series  name
                    # 234M      粉丝数
                    # 5.00      nox评分
                    # 英语      语言
                    # 娱乐 音乐 电影 流行音乐  tag
                    # 641.65K
                    # $ 72 USD
                    # 4.58%
                    # """
                    # writer.writerow(data_row)
                #根据实际情况，使用mysql存储更好，便于处理和修改某条数据，后续再导出为excel
            print("第{}列表页完成".format(wh_list_index))
            #更新wh_list_index
            wh_list_index+=1
            time.sleep(3)
            # print('修改被存储的索引')
            # sql = "insert into `nox_wh_index`(`wh_list_index`) values('{}');".format(wh_list_index)
            sql = "UPDATE `nox_wh_index` SET `wh_list_index`={};".format(wh_list_index)
            # print(sql)
            try:
                with connection.cursor() as cur:
                    cur.execute(sql)  # 保险起见，不使用批量，而是一条条
                    connection.commit()  # 如果数据库连接未配置为autocommit，则需要提交语句没有这个不会生效
            except Exception as e:
                print('第{}页失败'.format(wh_list_index))
                print(e)
            print('开始刷新下一页第{}页列表'.format(wh_list_index))






        #针对网红详情页 ，暂时停止
        # try:
        #     #单个详情页
        #     wh_2='https://cn.noxinfluencer.com/youtube/channel/UCq-Fj5jknLsUf-MWSy4_brA'
        #     driver.get(wh_2)
        # except TimeoutError as e:
        #     MyLibrary().keybd_event(27)  #设置超过加载时间就强停
        #详情页find

        # print(len('https://www.youtube.com/channel/UCoC47do520os_4DBMEFGg4A'))
        # print(len('https://www.facebook.com/cnliziqi'))
        # print(len('http://www.twitter.com/tseries'))
        # print(len('https://instagram.com/tseries.official'))


        # time.sleep(0.1)
        # get_html()
        #
        # time.sleep(30)
        # driver.quit() #关闭所有窗口
        #无限循环
        # while True:
        #     q=input=('q:')
        #     if q=='q':
        #         break















