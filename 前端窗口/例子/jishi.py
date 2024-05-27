import tkinter as tk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("简单计时器")

        self.seconds = 0
        self.is_running = False

        # 创建标签用于显示计时器时间
        self.label = tk.Label(root, text="0秒", font=("Helvetica", 20))
        self.label.pack(pady=20)

        # 创建开始按钮
        self.start_button = tk.Button(root, text="开始", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        # 创建停止按钮
        self.stop_button = tk.Button(root, text="停止", command=self.stop_timer)
        self.stop_button.pack(side=tk.RIGHT, padx=10)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()

    def stop_timer(self):
        self.is_running = False

    def update_timer(self):
        if self.is_running:
            self.seconds += 1
            self.label.config(text=f"{self.seconds}秒")
            self.root.after(1000, self.update_timer)  # 每秒更新一次

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

