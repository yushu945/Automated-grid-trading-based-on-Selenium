# 导入模块
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
fox_optinon = webdriver.FirefoxOptions()

# 使用headless无界面浏览器模式
fox_optinon.add_argument('--headless')
fox_optinon.add_argument('--disable-gpu')
# 加载驱动
driver = webdriver.Firefox(options=fox_optinon)
driver.get('http://quote.eastmoney.com/sh510300.html')  # 沪深300ETF
# driver.get('http://quote.eastmoney.com/sh600156.html')  # 华升股份
# 等待两秒
# time.sleep(0.5)
wait = WebDriverWait(driver, 0)
# 等待需要加载的class属性出现
while True:
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'quote_quotenums')))
    Shares = driver.find_element_by_class_name('zxj')  # 获取当前股价
    all_Styg = driver.find_element_by_class_name('zd')  # 获取当前涨幅和百分比
    shares_text = Shares.text  # 股价文本化
    styg_text = all_Styg.text  # 将获取的数据文本化
    if styg_text[0] == '-':
        # 获取的数据为跌幅
        # 将获取的涨幅和百分比分开
        second_dash_index = styg_text.find('-', styg_text.find('-') + 1)  # 第二个-号下标
        Rise = styg_text[:second_dash_index]  # 涨幅
        percentage = styg_text[second_dash_index:]  # 百分比
        print('价格:' + shares_text)
        print('涨幅:' + Rise)
        print('百分比:' + percentage)
    else:
        '''
        当获取的数据为涨幅时;
        注:当前此方法只适用于ETF的0.001幅度的涨幅.
        '''
        Rise = styg_text[:5]
        percentage = styg_text[5:]
        print('价格:' + shares_text)
        print('涨幅:' + Rise)
        print('百分比:' + percentage)