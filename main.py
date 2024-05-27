# 导入函数库
import time
from datetime import datetime
from datetime import time as Time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 导入自编写的函数
from data_crud import insert_save_frist
from quantization_rules_2 import quantitfy

# 创建火狐浏览器驱动参数对象
fox_optinon = webdriver.FirefoxOptions()

# 使用headless无界面浏览器模式
fox_optinon.add_argument('--headless')
fox_optinon.add_argument('--disable-gpu')

# 建立全局参数
frist_Price = None  # 每天9：25-9：30间启动记录开盘价格
frist_Rise = None  # 记录开盘涨幅
frist_Pcage = None  # 记录开盘百分比
old_Price = '0'  # 发生交易前的比较值
old_Rise = '0'
old_Pcage = '0%'


# 建立主题函数
def All_Main(url):
    # 加载驱动
    driver = webdriver.Firefox(options=fox_optinon)
    driver.get(url)  # 打开沪深300ETF页面
    wait = WebDriverWait(driver, 0)
    stop_time = Time(15, 10, 0)  # 设定停止时间
    # 建立一个记录首价的判断数据
    judge = 1
    # 引入全局变量
    global frist_Price
    global frist_Rise
    global frist_Pcage
    global old_Price
    global old_Rise
    global old_Pcage

    # 通过循环持续获取页面中的相关数据
    while True:    # 循环条件可能需要修改为可自定义
        time.sleep(3)
        # 获取当前时间
        now_time = datetime.now().time()  # 获取当前时间
        # 这个位置添加一个时间判断，当大于指定时间后跳出循环并停止程序
        if now_time > stop_time:
            print('交易时间结束,停止程序')
            break

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'quote_quotenums')))
        # Shares = driver.find_element_by_class_name('zxj')  # 获取当前股价
        Shares = driver.find_element(by=By.CLASS_NAME, value='zxj')  # 获取当前股价
        # all_Styg = driver.find_element_by_class_name('zd')  # 获取当前涨幅和百分比
        all_Styg = driver.find_element(by=By.CLASS_NAME, value='zd')  # 获取当前涨幅和百分比
        shares_text = Shares.text  # 股价文本化
        styg_text = all_Styg.text  # 将获取的数据文本化
        if styg_text[0] == '-':  # 当涨跌幅为负数时
            # 获取的数据为跌幅
            # 将获取的涨幅和百分比分开
            second_dash_index = styg_text.find('-', styg_text.find('-') + 1)  # 第二个-号下标
            Rise = styg_text[:second_dash_index]  # 涨幅
            percentage = styg_text[second_dash_index:]  # 百分比
            ''' 在这个位置添加记录首价 '''
            if judge == 1:
                frist_Price = shares_text
                frist_Rise = Rise
                frist_Pcage = percentage
                # 将获取的数据存入数据库
                insert_save_frist(frist_Price, frist_Rise, frist_Pcage)
                judge = 0
            # # 这个位置是将第一次获取的数据赋值给需要对比的值
            # if judge == 0:
            #     # 只运行一次，没问题
            #     old_Price = frist_Price
            #     old_Rise = frist_Rise
            #     old_Pcage = frist_Pcage
            #     judge = 2
            '''
            在这个位置添加比较函数并将触发量化公式的时间存入数据表;
            返回发生交易时的数据
            '''
            print('价格:' + shares_text)
            old_Price,old_Rise,old_Pcage = quantitfy(old_Price,old_Rise,old_Pcage,shares_text,Rise,percentage)
            print(old_Price + '--' + old_Rise + '--' + old_Pcage)
            print('*' * 20)
            # print('价格:' + shares_text)
            # print('涨幅:' + Rise)
            # print('百分比:' + percentage)
        else:
            '''
            当获取的数据为涨幅时;
            注:当前此方法只适用于ETF的0.001幅度的涨幅.
            '''
            Rise = styg_text[:5]
            percentage = styg_text[5:]
            if judge == 1:
                frist_Price = shares_text
                frist_Rise = Rise
                frist_Pcage = percentage
                # 将获取的数据存入数据库
                insert_save_frist(frist_Price, frist_Rise, frist_Pcage)
                judge = 0
            '''
            在这个位置添加比较函数并将触发量化公式的时间存入数据表;
            返回发生交易时的数据
            '''
            print('价格:' + shares_text)
            old_Price,old_Rise,old_Pcage = quantitfy(old_Price,old_Rise,old_Pcage,shares_text,Rise,percentage)
            print(old_Price+'--'+old_Rise+'--'+old_Pcage)
            print('*' * 20)
            # print('价格:' + shares_text)
            # print('涨幅:' + Rise)
            # print('百分比:' + percentage)




if __name__ == '__main__':
    # 加入比较时间的判断来进行是否进入主函数
    other_time_after = Time(9, 25, 0)  # 创建开始前时间
    other_time_last = Time(15, 10, 0)  # 创建开始后函数
    # 创建一个死循环
    while True:
        current_time = datetime.now().time()  # 获取当前时间
        # 判断是否为当前时间 如果是就结束循环
        if other_time_after < current_time <other_time_last:
            print('开始量化交易!')
            url = 'http://quote.eastmoney.com/sh510300.html'
            All_Main(url)
            break
        else:
            if current_time > other_time_last:
                print('结束程序')
                break
            else:
                time.sleep(5)
                print('当前时间: ' + current_time.strftime('%H:%M:%S'))

    # url = 'http://quote.eastmoney.com/sh510300.html'
    # All_Main(url)

