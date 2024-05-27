# 导入模块
import tkinter as tk
from tkinter import *
import time
import pyautogui

# 创建父窗口类
class Main_Gui():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    # 设计窗口
    def Set_init_window(self):
        init_window_name = self.init_window_name  # 主页面
        init_window_name.title('自动量化交易程序')  # 标题
        # 设置窗口大小
        init_window_name.geometry('602x500')
        # 创建父窗口上的功能菜单
        main_menu = tk.Menu(init_window_name)
        main_menu.add_cascade(label='获取位置信息', command=self.get_mouse_and_data)  # 进去子窗口
        init_window_name.config(menu=main_menu)  # 显示在前端页面上
        # 创建下滑框
        # scrollbar_y = tk.Scrollbar(init_window_name)
        # scrollbar_y.place(x=100, y=100, relheight=0.27)

        '''创建输入框控件'''
        # Url输入框控件
        left_label_1 = tk.Label(init_window_name, text='股票网址: ', font=('蔚然雅黑', 12, 'bold'))
        left_label_1.place(x=10, y=10)
        self.left_entry_1 = tk.Entry(init_window_name, width=25)
        self.left_entry_1.place(x=100, y=10)
        self.left_entry_1.insert(0, '输入东方财富网个股网址')  # 提供注释

        # 股票代码输入框控件
        left_label_2 = tk.Label(init_window_name, text='股票代码: ', font=('蔚然雅黑', 12, 'bold'))
        left_label_2.place(x=10, y=40)
        self.left_entry_2 = tk.Entry(init_window_name, width=25)
        self.left_entry_2.place(x=100, y=40)
        self.left_entry_2.insert(0, '例: 510300')

        # 可用数量输入框控件
        left_label_3 = tk.Label(init_window_name, text='可用数量: ', font=('蔚然雅黑', 12, 'bold'))
        left_label_3.place(x=10, y=70)
        self.left_entry_3 = tk.Entry(init_window_name, width=25)
        self.left_entry_3.place(x=100, y=70)
        self.left_entry_3.insert(0, '可以卖出的股票数量')

        # 可用资金输入框控件
        left_label_4 = tk.Label(init_window_name, text='可用资金: ', font=('蔚然雅黑', 12, 'bold'))
        left_label_4.place(x=10, y=100)
        self.left_entry_4 = tk.Entry(init_window_name, width=25)
        self.left_entry_4.place(x=100, y=100)

        # 交易数量输入框控件
        left_label_5 = tk.Label(init_window_name, text='交易数量: ', font=('蔚然雅黑', 12, 'bold'))
        left_label_5.place(x=10, y=130)
        self.left_entry_5 = tk.Entry(init_window_name, width=25)
        self.left_entry_5.place(x=100, y=130)
        self.left_entry_5.insert(0, '每次交易的数量')

        # 买卖差值输入框控件
        left_label_6 = tk.Label(init_window_name, text='买卖差值: ', font=('蔚然雅黑', 12, 'bold'))
        left_label_6.place(x=10, y=160)
        self.left_entry_6 = tk.Entry(init_window_name, width=25)
        self.left_entry_6.place(x=100, y=160)
        self.left_entry_6.insert(0, '例: 1是差值为1或-1时发生买卖')

        # 设计开始按钮控件
        frist_begin_button = tk.Button(init_window_name, text='启动(每日首次)', command=quit)  # 函数未完成
        frist_begin_button.place(x=20, y=200)

        # 设计停止按钮控件
        frist_stop_button = tk.Button(init_window_name, text='停止', command=quit, width=10)  # 函数未完成
        frist_stop_button.place(x=190, y=200)

        # 设计分隔线控件
        dividing_line_1 = tk.Canvas(init_window_name, height=1000, width=2, bg='black')
        dividing_line_1.place(x=300, y=0)  # 中间分界线

        dividing_line_2 = tk.Canvas(init_window_name, height=2, width=298, bg='black')
        dividing_line_2.place(x=0, y=240)  # 每日首次和第二次开始的分界线


        '''创建第二次重启的功能区块'''

        #  交易股价输入框控件
        left_label_7 = tk.Label(init_window_name, text='交易股价:', font=('蔚然雅黑', 12, 'bold'))
        left_label_7.place(x=10, y=260)
        self.left_entry_7 = tk.Entry(init_window_name, width=25)
        self.left_entry_7.place(x=100, y=260)
        self.left_entry_7.insert(0, '停止前最后一次交易的价格')

        # 交易涨跌输入框控件
        left_label_8 = tk.Label(init_window_name, text='交易幅度:', font=('蔚然雅黑', 12, 'bold'))
        left_label_8. place(x=10, y=290)
        self.left_entry_8 = tk.Entry(init_window_name, width=25)
        self.left_entry_8.place(x=100, y=290)
        self.left_entry_8.insert(0, '停止前最后一次交易的涨幅')

        # 百分比输入框控件
        left_label_9 = tk.Label(init_window_name, text='百 分 比:', font=('蔚然雅黑', 12, 'bold'))
        left_label_9.place(x=10, y=320)
        self.left_entry_9 = tk.Entry(init_window_name, width=25)
        self.left_entry_9.place(x=100, y=320)
        self.left_entry_9.insert(0, '停止前最后一次交易的百分比')

        # 创建第二次启动的按钮
        second_begin_button = tk.Button(init_window_name, text='启动(首次之后)', command=quit)
        second_begin_button.place(x=20, y=360)

        # 创建第二次开启后的停止按钮
        second_stop_button = tk.Button(init_window_name, text='停止', command=quit, width=10)
        second_stop_button.place(x=190, y=360)

        # 设计第二功能区分割线
        dividing_line_3 = tk.Canvas(init_window_name, height=2, width=298, bg='black')
        dividing_line_3.place(x=0, y=400)  # 每日首次和第二次开始的分界线


        '''创建显示当前可用资源的数据'''

        # 创建显示当前可用股票数量功能
        left_label_10 = tk.Label(init_window_name, text='可用数量:', font=('蔚然雅黑', 12, 'bold'))
        left_label_10.place(x=10, y=420)
        # 创建显示具体数据的功能
        self.left_label_11 = tk.Label(init_window_name, text=0, font=('蔚然雅黑', 12, 'bold'))
        self.left_label_11. place(x=100, y=420)

        # 创建显示可用资金数量功能
        left_label_12 = tk.Label(init_window_name, text='可用资金:', font=('蔚然雅黑', 12, 'bold'))
        left_label_12.place(x=10, y=460)
        self.left_label_13 = tk.Label(init_window_name, text=0, font=('蔚然雅黑', 12, 'bold'))
        self.left_label_13.place(x=100, y=460)

        '''显示右侧中所有的股价功能'''

        # 显示股价
        right_label_1 = tk.Label(init_window_name, text='价格:', font=('蔚然雅黑', 14, 'bold'))
        right_label_1.place(x=390, y=10)
        self.right_label_2 = tk.Label(init_window_name, text=0.0, font=('蔚然雅黑', 14, 'bold'))
        self.right_label_2.place(x=450, y=10)

        # 显示幅度
        right_label_3 = tk.Label(init_window_name, text='幅度:', font=('蔚然雅黑', 12, 'bold'))
        right_label_3.place(x=340, y=45)
        self.right_label_4 = tk.Label(init_window_name, text=0.0, font=('蔚然雅黑', 12, 'bold'))
        self.right_label_4.place(x=390, y=45)

        # 显示百分比
        right_label_5 = tk.Label(init_window_name, text='百分比:', font=('蔚然雅黑', 12, 'bold'))
        right_label_5.place(x=450, y=45)
        self.right_label_6 = tk.Label(init_window_name, text='0.0%', font=('蔚然雅黑', 12, 'bold'))
        self.right_label_6.place(x=520, y=45)

        # 显示当前时间
        right_label_7 = tk.Label(init_window_name, text='当前时间:', font=('蔚然雅黑', 12, 'bold'))
        right_label_7.place(x=340, y=75)
        # self.timestr = tk.StringVar()  # 生成动态字符串
        self.right_label_8 = tk.Label(init_window_name, text='00:00:00', font=('蔚然雅黑', 13, 'bold'))
        self.right_label_8.place(x=430, y=75)
        # self.get_stock_data()  # 调用获取股票数据的函数

        # 画出右侧股价与交易记录之间的隔开线
        dividing_line_4 = tk.Canvas(init_window_name, height=2, width=295, bg='black')
        dividing_line_4.place(x=304, y=110)  # 每日首次和第二次开始的分界线

        '''设计交易记录的功能'''

        # 显示交易记录功能
        right_label_9 = tk.Label(init_window_name, text='交易记录:', font=('蔚然雅黑', 14, 'bold'))
        right_label_9.place(x=310, y=130)
        self.right_text_1 = tk.Text(init_window_name, width=38, height=25)
        self.right_text_1.place(x=315, y=168)
        return None


    # 建立动态获取时间的函数
    def get_stock_data(self):
        new_time = time.strftime('%H:%M:%S')
        self.right_label_8.config(text=new_time)
        self.init_window_name.after(2000, self.get_stock_data)
        return None


    # 创建获取鼠标坐标信息和保存自动化点击的坐标
    def get_mouse_and_data(self):
        # 创建一个子窗口
        self.get_mouse_window = tk.Toplevel()
        self.get_mouse_window.title('获取鼠标坐标信息并保存')  # 子窗口标题
        self.get_mouse_window.geometry('402x280')  # 设置子窗口大小

        # 设置一个启动获取鼠标信息的开关
        self.get_mouse_runing = False

        # 创建分界线
        dividing_line_5 = tk.Canvas(self.get_mouse_window, height=500, width=2, bg='black')
        dividing_line_5.place(x=200, y=0)  # 布置分界线位置

        # 创建获取信息功能标题
        label_getmouse_1 = tk.Label(self.get_mouse_window, text='获取鼠标位置信息:', font=('蔚然雅黑', 11, 'bold'))
        label_getmouse_1.place(x=0, y=5)

        # 创建获取鼠标坐标信息位置的功能按钮
        get_mouse_button_begin = tk.Button(self.get_mouse_window, text='开始', command=self.start_mouse, width=10)  # 开始功能按钮
        get_mouse_button_begin.place(x=10, y=35)
        get_mouse_button_stop = tk.Button(self.get_mouse_window, text='停止', command=self.stop_mouse, width=10)  # 停止功能按钮
        get_mouse_button_stop.place(x=110, y=35)

        '''保存具体数据'''
        # 创建标题
        label_getmouse_2 = tk.Label(self.get_mouse_window, text='保存具体信息:', font=('蔚然雅黑', 12, 'bold'))
        label_getmouse_2.place(x=0, y=83)

        # 画线隔离功能按钮
        dividing_line_6 = tk.Canvas(self.get_mouse_window, height=2, width=198, bg='black')
        dividing_line_6.place(x=0, y=73)

        # 保存进入页面功能的x、y轴
        label_getmouse_3 = tk.Label(self.get_mouse_window, text='进入页面: X轴:')  # 保存x轴提示框
        label_getmouse_3.place(x=0, y=115)
        self.entry_getmouse_1 = tk.Entry(self.get_mouse_window, width=5)  # x轴输入框
        self.entry_getmouse_1.place(x=86, y=115)
        label_getmouse_4 = tk.Label(self.get_mouse_window, text='Y轴:')  # Y轴提示框
        label_getmouse_4.place(x=124, y=115)
        self.entry_getmouse_2 = tk.Entry(self.get_mouse_window, width=5)  # Y轴输入框
        self.entry_getmouse_2.place(x=154, y=115)

        # 保存点击买卖功能的x、y轴
        label_getmouse_5 = tk.Label(self.get_mouse_window, text='点击买卖: X轴:')  # 保存x轴提示框
        label_getmouse_5.place(x=0, y=145)
        self.entry_getmouse_3 = tk.Entry(self.get_mouse_window, width=5)  # x轴输入框
        self.entry_getmouse_3.place(x=86, y=145)
        label_getmouse_6 = tk.Label(self.get_mouse_window, text='Y轴:')  # Y轴提示框
        label_getmouse_6.place(x=124, y=145)
        self.entry_getmouse_4 = tk.Entry(self.get_mouse_window, width=5)  # Y轴输入框
        self.entry_getmouse_4.place(x=154, y=145)

        # 保存点击是功能的x、y轴
        label_getmouse_7 = tk.Label(self.get_mouse_window, text='点 击 是:  X轴:')  # 保存x轴提示框
        label_getmouse_7.place(x=0, y=175)
        self.entry_getmouse_5 = tk.Entry(self.get_mouse_window, width=5)  # x轴输入框
        self.entry_getmouse_5.place(x=86, y=175)
        label_getmouse_8 = tk.Label(self.get_mouse_window, text='Y轴:')  # Y轴提示框
        label_getmouse_8.place(x=124, y=175)
        self.entry_getmouse_6 = tk.Entry(self.get_mouse_window, width=5)  # Y轴输入框
        self.entry_getmouse_6.place(x=154, y=175)

        # 保存点击买卖功能的x、y轴
        label_getmouse_9 = tk.Label(self.get_mouse_window, text='点击确认: X轴:')  # 保存x轴提示框
        label_getmouse_9.place(x=0, y=205)
        self.entry_getmouse_7 = tk.Entry(self.get_mouse_window, width=5)  # x轴输入框
        self.entry_getmouse_7.place(x=86, y=205)
        label_getmouse_10 = tk.Label(self.get_mouse_window, text='Y轴:')  # Y轴提示框
        label_getmouse_10.place(x=124, y=205)
        self.entry_getmouse_8 = tk.Entry(self.get_mouse_window, width=5)  # Y轴输入框
        self.entry_getmouse_8.place(x=154, y=205)

        # 设置保存按钮
        get_mouse_button_save = tk.Button(self.get_mouse_window, text='保存', command=quit, width=10)  # 开始功能按钮
        get_mouse_button_save.place(x=10, y=235)

        '''设置位置信息'''

        # 显示鼠标位置信息
        label_getmouse_11 = tk.Label(self.get_mouse_window, text='鼠标位置信息:', font=('蔚然雅黑', 11, 'bold'))
        label_getmouse_11.place(x=205, y=5)

        # 创建实时显示当前位置信息的text框
        self.getmouse_text_1 = tk.Text(self.get_mouse_window, height=18, width=27)  # 显示鼠标信息的框
        self.getmouse_text_1.place(x=207, y=35)
        return

    # 创建开始获取鼠标信息的函数
    def start_mouse(self):
        self.getmouse_text_1.delete(1.0, tk.END)
        # 测试实现在print中输出鼠标数据
        if not self.get_mouse_runing:
            self.get_mouse_runing = True
            self.updata_mouse()
        return None

    # 创建停止按钮的模块
    def stop_mouse(self):
        self.get_mouse_runing = False
        return None

    # 创建运行获取鼠标信息功能的函数
    def updata_mouse(self):
        if self.get_mouse_runing:
            mouse_x, mouse_y = pyautogui.position()
            data = '当前鼠标位置信息: X: ' + str(mouse_x) + '  Y: ' + str(mouse_y)
            self.getmouse_text_1.insert(tk.END, data + "\n")
            self.get_mouse_window.after(5000, self.updata_mouse)




if __name__ == "__main__":
    init_Windows = tk.Tk()  # 创建一个父窗口
    Gui = Main_Gui(init_Windows)
    Gui.Set_init_window()
    # Gui.get_mouse_and_data()  # 测试用，用后删
    init_Windows.mainloop()
