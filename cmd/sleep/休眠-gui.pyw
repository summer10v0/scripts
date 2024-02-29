import tkinter as tk
import ctypes
import os
import subprocess

def turn_off_display():
    SC_MONITORPOWER = 0xF170
    WM_SYSCOMMAND = 0x0112
    HWND_BROADCAST = 0xFFFF
    SW_HIDE = 2

    ctypes.windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, SW_HIDE)

def lock_screen():
    ctypes.windll.user32.LockWorkStation()

def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState")

def hibernate():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def restart():
    os.system("shutdown /r")

def shutdown():
    os.system("shutdown /s")

def slidetoshutdown():
    subprocess.run("Slidetoshutdown")

def cancel_shutdown():
    os.system("shutdown /a")

def create_window():
    window = tk.Tk()
    window.title("系统操作")

    # 设置窗口的大小
    window.geometry("600x400")

    # 将窗口移动到屏幕中央
    window.update()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    position_right = int(window.winfo_screenwidth()/2 - window_width/2)
    position_down = int(window.winfo_screenheight()/2 - window_height/2)
    window.geometry("+{}+{}".format(position_right, position_down))

    # 设置窗口和Frame的背景颜色
    window.configure(bg="#ffdab9")
    frame = tk.Frame(window, bg="#ffdab9")
    frame.pack(expand=True)

    # 创建并布局按钮
    commands = [turn_off_display, lock_screen, sleep, hibernate, restart, shutdown, slidetoshutdown, cancel_shutdown]
    texts = ["息屏", "锁屏", "睡眠", "休眠", "重启", "关机", "滑动关机", "取消关机"]
    for i in range(4):
        for j in range(2):
            button = tk.Button(frame, 
                               text=texts[i*2+j], 
                               command=commands[i*2+j], 
                               width=20, 
                               height=2, 
                               font=("方正宋黑简体", 16), 
                               fg="#8b4513", 
                               bg="#ffdead", 
                               activebackground="#ffa07a")
            button.grid(row=i, column=j, padx=10, pady=10, sticky="nsew")

    window.mainloop()

if __name__ == "__main__":
    create_window()