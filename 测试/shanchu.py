import tkinter as tk
import pyautogui
import time

def clear_text():
    # 设置焦点到Text小部件
    text.focus()

    # 模拟按键操作来清空Text小部件
    pyautogui.hotkey('ctrl', 'a')  # 选择所有文本
    pyautogui.press('backspace')   # 删除选中的文本

# 创建主窗口
root = tk.Tk()
root.title("使用pyautogui清空Text输入框中的数据")

# 创建Text输入框
text = tk.Text(root, height=10, width=40)
text.pack(padx=10, pady=10)
text.insert(tk.END, "这是一些示例文本。")

# 创建按钮，点击按钮时清空Text输入框中的数据
clear_button = tk.Button(root, text="清空数据", command=clear_text)
clear_button.pack(pady=10)

# 运行主循环
root.mainloop()