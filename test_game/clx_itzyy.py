from PIL import ImageGrab
from memory_pic import *
import aircv as ac
import win32con
import win32api
import win32gui
import autopy
import time
import os, sys
import multiprocessing
import easygui
import base64
import pymysql


def get_winds():
    hwnd1 = win32gui.FindWindowEx(0, 0, "Messiah_Game", "一梦江湖")
    win32gui.ShowWindow(hwnd1, win32con.SW_RESTORE)
    win32gui.SetWindowPos(hwnd1, win32con.HWND_TOPMOST, 436, 107, 1064, 572, win32con.SWP_SHOWWINDOW)


def get_src():
    abspath = os.getcwd()
    filename = "\\src.jpg"
    win32api.keybd_event(win32con.VK_SNAPSHOT, 0)
    time.sleep(0.5)
    src = ImageGrab.grabclipboard()
    src.save(abspath+filename)


def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()


def logs(info):
    with open('logs.text', mode='a+', encoding='GBK') as f:
        f.write(info + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n')


def get_pics():
    get_pic(test1_png, 'test1.png')
    get_pic(test2_png, 'test2.png')
    get_pic(test3_png, 'test3.png')
    get_pic(test4_png, 'test4.png')
    get_pic(test5_png, 'test5.png')
    get_pic(test6_png, 'test6.png')
    get_pic(test7_png, 'test7.png')
    get_pic(test8_png, 'test8.png')
    get_pic(shou_png, 'shou.png')
    get_pic(not_png, 'not.png')
    get_pic(not2_png, 'not2.png')
    get_pic(oneline_png, 'oneline.png')
    get_pic(towline_png, 'towline.png')
    get_pic(threeline_png, 'threeline.png')


def compare_(objs):
    imobj = ac.imread(objs)
    imsrc = ac.imread('%s\\src.jpg' % os.getcwd())
    pos = ac.find_template(imsrc, imobj, 0.5)
    return pos


def get_user(sql):
    result = None
    try:
        conn = pymysql.connect(host='12.34.56.789', port=3306, db='chuliuxiang', user='root', passwd='自己的密码')
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        logs('%s' % e)
    return result


def changge_flag(num):
    while num.value:
        title = '傻瓜请登录'
        msg = '请输入变瓜码'
        login = easygui.multpasswordbox(msg, title, (['用户名:', '密码:']))
        username = 'zyy'
        password = 123456
        try:
            username = login[0]
            password = int(login[1])
        except Exception as e:
            logs('%s' % e)
        res = get_user("select username  from user where username='%s' and password=%d" % (username, password))
        if res:
            while True:
                a = easygui.choicebox(msg='一梦江湖辅助', title='itzyy', choices=('退出程序', '塞北黄金(换线)', '塞北立银(换线)', '定点挖砍(换线)', '定点挖砍(不换线)'))
                if a == '塞北黄金(换线)':
                    a = 1
                elif a == '塞北立银(换线)':
                    a = 2
                elif a == '定点挖砍(换线)':
                    a = 3
                elif a == '定点挖砍(不换线)':
                    a = 21
                elif a == '退出程序':
                    a = 0
                else:
                    a = 100
                try:
                    num.value = int(a)
                    if num.value == 0:
                        break
                except Exception as e:
                    logs('%s' % e)
                time.sleep(2)


def mnings(num):
    def good():
        if num.value == 1:
            logs('开始挖金矿')
            mning = Mning()
            get_src()
            nums = 0
            while num.value:
                lists = []
                lists.append(compare_("test7.png")['confidence'] if compare_("test7.png") != None else 0)
                lists.append(compare_("test8.png")['confidence'] if compare_("test8.png") != None else 0)
                lists.append(compare_("test2.png")['confidence'] if compare_("test2.png") != None else 0)
                confidence = max(lists)
                shou = compare_("shou.png")['confidence'] if compare_("shou.png") != None else 0
                if confidence >= 0.6 or shou >= 0.9:
                    mning.all()
                    time.sleep(10)
                    mning.find_gold()
                    time.sleep(4)
                    get_src()
                else:
                    mning.find_gold()
                    time.sleep(2)
                    get_src()
                    nums += 1
                if nums == 5:
                    break
        if num.value == 2:
            logs('开始挖立银')
            mning = Mning()
            get_src()
            nums = 0
            while num.value:
                lists = []
                lists.append(compare_("test2.png")['confidence'] if compare_("test2.png") != None else 0)
                lists.append(compare_("test4.png")['confidence'] if compare_("test4.png") != None else 0)
                lists.append(compare_("test5.png")['confidence'] if compare_("test5.png") != None else 0)
                lists.append(compare_("test6.png")['confidence'] if compare_("test6.png") != None else 0)
                confidence = max(lists)
                shou = compare_("shou.png")['confidence'] if compare_("shou.png") != None else 0
                if confidence >= 0.7 or shou >= 0.9:
                    mning.all()
                    time.sleep(10)
                    mning.find_mning()
                    time.sleep(6)
                    get_src()
                else:
                    mning.find_mning()
                    time.sleep(4)
                    get_src()
                    nums += 1
                if nums == 4:
                    break
        if num.value == 3:
            logs('定点换线')
            mning = Mning()
            nums = 0
            while num.value:
                time.sleep(1)
                mning.all()
                time.sleep(8)
                nums += 1
                if nums == 4:
                    break

    autopy.mouse.move(1060, 545)
    autopy.mouse.click()
    time.sleep(3)
    while num.value:
        if num.value in [1, 2, 3]:

            change_line("oneline")
            time.sleep(5)
            get_src()
            good()
            logs('一线完成')

            tow = change_line("towline")
            if tow == 1:
                continue
            else:
                time.sleep(5)
                get_src()
                good()
                logs('二线完成')

            three = change_line("threeline")
            if three == 1:
                continue
            else:
                time.sleep(5)
                get_src()
                good()
                logs('三线完成')

        if num.value >= 20:
            time.sleep(3)
            if num.value == 21:
                logs('定点不换线')
                mning = Mning()
                while num.value:
                    time.sleep(2)
                    mning.all()
                    time.sleep(8)


class Mning():
    def mouse_click(self, x, y):
        autopy.mouse.move(x, y)
        autopy.mouse.click()

    def do_it(self):
        self.mouse_click(1170, 411)

    def change(self):
        self.mouse_click(1090, 360)

    def shop(self):
        self.mouse_click(960, 510)
        time.sleep(0.5)
        self.mouse_click(1120, 510)
        time.sleep(0.5)
        self.mouse_click(790, 570)

    def find_mning(self):
        self.mouse_click(1460, 165)
        time.sleep(2)
        self.mouse_click(1040, 545)
        time.sleep(2)
        self.mouse_click(1460, 165)

    def find_gold(self):
        self.mouse_click(1460, 165)
        time.sleep(2)
        self.mouse_click(1060, 545)
        time.sleep(2)
        self.mouse_click(1460, 165)

    def find_tree(self):
        self.mouse_click(1460, 165)
        time.sleep(1.5)
        self.mouse_click(1070, 415)
        time.sleep(1)
        self.mouse_click(1460, 165)

    def all(self):
        self.do_it()
        time.sleep(0.5)
        self.change()


def change_line(line):
    logs('启动换线功能')
    try:
        time.sleep(2)
        autopy.mouse.move(1480, 160)
        autopy.mouse.click()
        time.sleep(2)
        get_src()

        lines = compare_("%s.png" % line)

        x1 = 1240
        y1 = 202

        x2 = 1240
        y2 = 252

        x3 = 1240
        y3 = 302

        confidence = lines['confidence'] if lines else 0

        if line == "oneline" and confidence >= 0.9:
            autopy.mouse.move(x1, y1)
            autopy.mouse.click()
            time.sleep(2)
            logs('进入一线')
        elif line == "towline" and confidence >= 0.9:
            autopy.mouse.move(x2, y2)
            autopy.mouse.click()
            time.sleep(2)
            logs('进入二线')
        elif line == "threeline" and confidence >= 0.98:
            autopy.mouse.move(x3, y3)
            autopy.mouse.click()
            time.sleep(2)
            logs('进入三线')
        else:
            autopy.mouse.move(1460, 160)
            autopy.mouse.click()
            logs(line + '未找到重启换线')
            return 1
    except Exception as e:
        logs('%s' % e)


if __name__ == '__main__':

    multiprocessing.freeze_support()
    get_pics()
    get_winds()
    time.sleep(2)
    num = multiprocessing.Value("d", 10.0)
    p_input = multiprocessing.Process(target=changge_flag, args=(num,))
    p_input.start()
    logs('界面程序已启动')
    p_mning = multiprocessing.Process(target=mnings, args=(num,))
    p_mning.start()
    logs('主程序启动')






