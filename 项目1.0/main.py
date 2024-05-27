import pyautogui as pg
import time

'''
该项目主要实现目的:
1.通过死循环对屏幕进行不停的截图。
2.在循环中对获取的图片进行读取。
3.对读取的数据进行处理判断.
4.将判断的数据获取的处理方式实现
'''

# 创建一个获取屏幕截图的死循环类
class PgCv_Run():

    def __init__(self):
        pass

    # 设置一个函数使用pyautogui的截图功能
    def get_screenshots(self):
        self.Screenshot = pg.screenshot(region=(0, 0, 800, 600))  # region中参数暂时为这些
        self.Screenshot.save('图片/屏幕截图.png')  # 将获取的屏幕截图存储在指定位置
        print('截图保存成功!')
        # 这个位置需要添加一个函数来将获取的图片进行处理 PS:建议使用opcv
        '''需要使用到深度学习的内容  使用tensorflow'''
        return None
    # 建立函数对图片数据进行处理
    def opcv_dispose(self):

        return None



if __name__ == '__main__':
    run = PgCv_Run()
    run.get_screenshots()
    # while True:
    #     time.sleep(3)
    #     PgCv_Run()