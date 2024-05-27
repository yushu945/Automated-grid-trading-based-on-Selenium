import tkinter as tk
import pyautogui

def update_mouse_position():
    x, y = pyautogui.position()
    position_label.config(text=f"鼠标位置: X={x}, Y={y}")
    root.after(5000, update_mouse_position)  # 每100毫秒更新一次

# 创建主窗口
root = tk.Tk()
root.title("实时获取鼠标位置")

# 创建Label用于显示鼠标位置信息
position_label = tk.Label(root, text="鼠标位置: X=0, Y=0", font=("Helvetica", 14))
position_label.pack(pady=10)

# 调用update_mouse_position函数开始实时获取鼠标位置
update_mouse_position()

# 运行主循环
root.mainloop()

