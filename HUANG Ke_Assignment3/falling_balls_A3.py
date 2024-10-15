import tkinter as tk
import random



# 创建窗口
window = tk.Tk()
window.title("鼠标移动的小球掉落")
window.geometry("800x600")

# 创建画布
canvas = tk.Canvas(window, bg="white", width=800, height=600)
canvas.pack()

# 定义函数，在鼠标移动时创建小球
def create_ball(event):
    # 小球的初始位置是鼠标所在位置
    x = event.x
    y = event.y
    
    # 小球的随机大小和颜色
    size = random.randint(10, 30)
    color = "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
    
    # 创建小球
    ball = canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)
    
    # 定义小球下落的动画
    def move_ball():
        nonlocal y
        if y < 600 - size:
            canvas.move(ball, 0, 5)  # 小球每次下落5个像素
            y += 5
            window.after(50, move_ball)  # 50毫秒后再次调用move_ball
        else:
            canvas.delete(ball)  # 小球到达底部时删除
    
    move_ball()

# 绑定鼠标移动事件到create_ball函数
canvas.bind('<Motion>', create_ball)

# 启动主循环
window.mainloop()
