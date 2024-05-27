import tkinter as tk

def clear_text():
    text.delete(1.0, tk.END)

# 创建主窗口
root = tk.Tk()
root.title("清空Text控件数据")

# 创建Text控件
text = tk.Text(root, height=10, width=40)
text.pack(padx=10, pady=10)

# 创建按钮，点击按钮时清空Text控件数据
clear_button = tk.Button(root, text="清空数据", command=clear_text)
clear_button.pack(pady=10)

# 运行主循环
root.mainloop()
