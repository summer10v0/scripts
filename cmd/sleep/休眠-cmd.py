import ctypes
import os
import sys
import subprocess

def turn_off_display():
    SC_MONITORPOWER = 0xF170
    WM_SYSCOMMAND = 0x0112
    HWND_BROADCAST = 0xFFFF
    SW_HIDE = 2

    ctypes.windll.user32.PostMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, SW_HIDE)

def lock_screen():
    ctypes.windll.user32.LockWorkStation()

def show_menu():
    print("请输入以下数字，确认对应操作：")
    print("1. 息屏")
    print("2. 锁屏")
    print("3. 睡眠")
    print("4. 休眠")
    print("5. 重启")
    print("6. 关机")
    print("7. 滑动关机")
    print("8. 取消关机")
    print("其他任意键退出")

def execute_command(choice):
    if choice == '1':
        turn_off_display()
    elif choice == '2':
        lock_screen()
    elif choice == '3':
        os.system("rundll32.exe powrprof.dll,SetSuspendState")
    elif choice == '4':
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif choice == '5':
        os.system("shutdown /r")
    elif choice == '6':
        os.system("shutdown /s")
    elif choice == '7':
        subprocess.run("Slidetoshutdown")
    elif choice == '8':
        os.system("shutdown /a")
    else:
        sys.exit()

def main():
    while True:
        show_menu()
        choice = input()
        execute_command(choice)

if __name__ == "__main__":
    main()