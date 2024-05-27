import pyautogui as pg



'''
region（可选）：一个元组，用于指定截图的区域。
其中，(x, y) 是截图的起始坐标，width 是截图的宽度，height 是截图的高度。
如果不提供 region 参数，则默认截取整个屏幕。
'''
screenshot = pg.screenshot(region=(0,0,800,600))
screenshot.save('图片/屏幕截图.png')