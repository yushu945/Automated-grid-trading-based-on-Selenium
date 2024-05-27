import pyautogui
import time
# 获取当前鼠标的 x 和 y 坐标
'''
当前鼠标坐标：(681, 118)  点击国盛证券页面位置
当前鼠标坐标：(284, 125)  # 输入代码
当前鼠标坐标：(272, 208)  # 输入 数量
当前鼠标坐标：(306, 245)  # 点击买入 
当前鼠标坐标：(329, 359)  # 点击是
当前鼠标坐标：(402, 314)  # 点击确认
'''
while True:
    time.sleep(5)
    mouse_x, mouse_y = pyautogui.position()

    # 打印坐标信息
    print(f"当前鼠标坐标：({mouse_x}, {mouse_y})")



