# import tkinter as tk
#
# def left_button_click():
#     print("Left button clicked")
#
# def right_button_click():
#     print("Right button clicked")
#
# # 创建主窗口
# root = tk.Tk()
# root.title("分成两个部分的页面")
#
# # 创建左侧Frame
# left_frame = tk.Frame(root, width=200, height=400, bg="lightblue")
# left_frame.pack(side=tk.LEFT, padx=10, pady=10)
#
# # 在左侧Frame中添加按钮
# left_button = tk.Button(left_frame, text="左侧按钮", command=left_button_click)
# left_button.pack(pady=10)
#
# # 创建右侧Frame
# right_frame = tk.Frame(root, width=200, height=400, bg="lightgreen")
# right_frame.pack(side=tk.RIGHT, padx=10, pady=10)
#
# # 在右侧Frame中添加按钮
# right_button = tk.Button(right_frame, text="右侧按钮", command=right_button_click)
# right_button.pack(pady=10)
#
# # 运行主循环
# root.mainloop()

import tkinter as tk

def left_button_click():
    print("Left button clicked")

def right_button_click():
    print("Right button clicked")

# 创建主窗口
root = tk.Tk()
root.title("分成两个部分的页面")

# 创建左侧Frame
left_frame = tk.Frame(root, width=200, height=400, bg="lightblue")
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

# 在左侧Frame中添加按钮
left_button = tk.Button(left_frame, text="左侧按钮", command=left_button_click)
left_button.pack(pady=20)

# 创建分隔线
separator = tk.Canvas(root, height=400, width=2, bg="black")
separator.pack(side=tk.LEFT, padx=5)

# 创建右侧Frame
right_frame = tk.Frame(root, width=200, height=400, bg="lightgreen")
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# 在右侧Frame中添加按钮
right_button = tk.Button(right_frame, text="右侧按钮", command=right_button_click)
right_button.pack(pady=10)

# 运行主循环
root.mainloop()

