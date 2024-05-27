import tkinter as tk

def update_label_text():
    initial = initial_text  # 获取Entry中的文本
    initial = initial - 100
    label.config(text=initial)  # 更新Label的文本

# 创建主窗口
root = tk.Tk()
root.title("修改Label数据的例子")

# 创建Entry小部件
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# 创建按钮，点击按钮时更新Label的文本
update_button = tk.Button(root, text="更新Label文本", command=update_label_text)
update_button.pack(pady=10)

# 创建初始的Label
initial_text = 500
label = tk.Label(root, text=initial_text)
label.pack(pady=10)

# 运行主循环
root.mainloop()
