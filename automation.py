# 导入模块
import pyautogui
import time

'''
当前鼠标坐标：(293, 680)
当前鼠标坐标：(298, 723)
当前鼠标坐标：(300, 761)
当前鼠标坐标：(310, 806)
当前鼠标坐标：(742, 694)  # 点击位置
鼠标点击完成路径
当前鼠标坐标：(330, 807)  # 买
当前鼠标坐标：(381, 914)  # 是
当前鼠标坐标：(442, 869)  # 确定
'''

'''当前鼠标坐标：(705, 570)
当前鼠标坐标：(380, 659)
当前鼠标坐标：(368, 765)
当前鼠标坐标：(381, 811)'''
# 建立国元证券急速买入函数
def GuoYuan_Buy_stock(number):
    # 鼠标指针进入指定的交易系统界面
    pyautogui.click(x=705, y=570)
    time.sleep(0.5)  # 暂停0.5s
    # 模拟键盘按下F1 进入交易系统买入界面
    pyautogui.keyDown('F1')
    pyautogui.keyUp('F1')
    pyautogui.click(x=380, y=659)
    time.sleep(0.5)  # 暂停0.5s
    # 输入证券代码  PS:暂时为固定的代码，之后会改进(510300)沪深300ETF
    pyautogui.typewrite('510300')  # 暂时固定
    time.sleep(0.5)  # 暂停0.5s
    # 点击买入数量方框位置
    pyautogui.click(x=368, y=765)
    pyautogui.typewrite(str(number))  # 输入的数据只能为字符类型
    time.sleep(0.5)  # 暂停0.5s
    # 实现买入
    pyautogui.click(x=381, y=811)  # 点击买入
    time.sleep(0.5)  # 暂停0.5s
    pyautogui.click(x=380, y=903)  # 点击是
    time.sleep(0.5)  # 暂停0.5s
    pyautogui.click(x=449, y=851)  # 点击确认
    # pyautogui.keyDown('B')
    # pyautogui.keyDown('Y')
    # pyautogui.keyUp('B')
    # pyautogui.keyUp('Y')
    # time.sleep(0.5)
    # pyautogui.keyDown('Enter')
    # pyautogui.keyUp('Enter')
    return None

# 建立国元证券急速卖出函数
def GuoYuan_Sell_stock(number):
    # 鼠标指针进入指定的交易系统界面
    pyautogui.click(x=705, y=570)
    time.sleep(0.5)  # 暂停0.5s
    # 模拟键盘按下F1 进入交易系统买入界面
    pyautogui.keyDown('F2')
    pyautogui.keyUp('F2')
    pyautogui.click(x=380, y=659)
    time.sleep(0.5)  # 暂停0.5s
    # 输入证券代码  PS:暂时为固定的代码，之后会改进(510300)沪深300ETF
    pyautogui.typewrite('510300')  # 暂时固定
    time.sleep(0.5)  # 暂停0.5s
    # 点击买入数量方框位置
    pyautogui.click(x=368, y=765)
    pyautogui.typewrite(str(number))  # 输入的数据只能为字符类型
    time.sleep(0.5)  # 暂停0.5s
    # 实现买入
    pyautogui.click(x=381, y=811)  # 点击买入
    time.sleep(0.5)  # 暂停0.5s
    pyautogui.click(x=380, y=903)  # 点击是
    time.sleep(0.5)  # 暂停0.5s
    pyautogui.click(x=449, y=851)  # 点击确认
    # pyautogui.keyDown('S')
    # pyautogui.keyDown('Y')
    # pyautogui.keyUp('S')
    # pyautogui.keyUp('Y')
    # time.sleep(0.5)
    # pyautogui.keyDown('Enter')
    # pyautogui.keyUp('Enter')
    return None



'''
当前鼠标坐标：(681, 118)  点击国盛证券页面位置
当前鼠标坐标：(284, 125)  # 输入代码
当前鼠标坐标：(272, 208)  # 输入 数量
当前鼠标坐标：(306, 245)  # 点击买入 
当前鼠标坐标：(329, 359)  # 点击是
当前鼠标坐标：(402, 314)  # 点击确认
'''

'''当前鼠标坐标：(120, 144)
当前鼠标坐标：(385, 151)
当前鼠标坐标：(352, 257)
当前鼠标坐标：(377, 313)
当前鼠标坐标：(405, 377)
当前鼠标坐标：(491, 324)'''
# 建立国盛证券的急速买入程序
def GuoSheng_Buy_stock(number, price_number):
    # 鼠标指针进入指定的交易系统界面
    pyautogui.click(x=120, y=144)
    time.sleep(0.5)  # 暂停0.5s
    # 模拟键盘按下F1 进入交易系统买入界面
    pyautogui.keyDown('F1')
    pyautogui.keyUp('F1')
    pyautogui.click(x=385, y=151)
    time.sleep(0.5)  # 暂停0.5s
    # 输入证券代码  PS:暂时为固定的代码，之后会改进(510300)沪深300ETF
    pyautogui.typewrite('510300')  # 暂时固定
    time.sleep(0.5)  # 暂停0.5s
    # 点击买入价格方框位置
    pyautogui.click(x=380, y=207)
    time.sleep(0.5)
    # 模拟删除数字
    for _ in range(5):
        pyautogui.press('backspace')
        time.sleep(0.05)
    pyautogui.typewrite(str(price_number))
    # 点击买入数量方框位置
    pyautogui.click(x=352, y=257)
    pyautogui.typewrite(str(number))  # 输入的数据只能为字符类型
    time.sleep(0.5)  # 暂停0.5s
    # 实现买入
    pyautogui.click(x=377, y=313)  # 点击买入
    time.sleep(0.5)  # 暂停0.5s
    pyautogui.click(x=427, y=359)  # 点击是
    time.sleep(0.5)  # 暂停0.5s
    pyautogui.click(x=485, y=301)  # 点击确认
    return None


# 建立国盛证券急速卖出函数
def GuoSheng_Sell_stock(number, price_number):
    # 鼠标指针进入指定的交易系统界面
    pyautogui.click(x=120, y=144)
    time.sleep(0.5)  # 暂停0.5s
    # 模拟键盘按下F1 进入交易系统买入界面
    pyautogui.keyDown('F2')
    pyautogui.keyUp('F2')
    pyautogui.click(x=385, y=151)
    time.sleep(0.5)  # 暂停0.5s
    # 输入证券代码  PS:暂时为固定的代码，之后会改进(510300)沪深300ETF
    pyautogui.typewrite('510300')  # 暂时固定
    time.sleep(0.5)  # 暂停0.5s
    # 点击买入价格方框位置
    pyautogui.click(x=380, y=207)
    time.sleep(0.5)
    # 模拟删除数字
    for _ in range(5):
        pyautogui.press('backspace')
        time.sleep(0.05)
    pyautogui.typewrite(str(price_number))

    # 点击买入数量方框位置
    pyautogui.click(x=352, y=257)
    pyautogui.typewrite(str(number))  # 输入的数据只能为字符类型
    time.sleep(0.5)  # 暂停0.5s
    # 实现买入
    pyautogui.click(x=377, y=313)  # 点击买入
    time.sleep(0.5)  # 暂停0.5s
    pyautogui.click(x=427, y=359)  # 点击是
    time.sleep(0.5)  # 暂停0.5s
    pyautogui.click(x=485, y=301)  # 点击确认
    return None

#  测试函数  当前鼠标坐标：(336, 207)==>买入价格
def ceshi(number):
    pyautogui.click(x=120, y=144)
    time.sleep(0.5)
    pyautogui.click(x=385, y=151)
    time.sleep(0.5)  # 暂停0.5s
    # 输入证券代码  PS:暂时为固定的代码，之后会改进(510300)沪深300ETF
    pyautogui.typewrite('510300')  # 暂时固定
    time.sleep(0.5)  # 暂停0.5s
    pyautogui.click(x=380, y=207)
    time.sleep(0.5)
    for _ in range(5):
        pyautogui.press('backspace')
        time.sleep(0.1)
    pyautogui.typewrite(str(number))



if __name__ == '__main__':
    # GuoYuan_Sell_stock(100)
    GuoSheng_Sell_stock(100, 3.425)
    # ceshi(3.425)