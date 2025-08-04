# utils.py
import tkinter as tk
from datetime import datetime
import sys
from tkinter import simpledialog

# 定义全局变量
deck = []
discard_deck = []
text = None  # 用于存储Text控件的引用
window = None  # 用于存储Tk窗口的引用
def log(msg: str, level: int, textv=text):
    '''
    自定义日志函数
    '''
    if textv is None:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Error: textv is None, cannot log to GUI")
        return

    if level == 0:  # Debug级别日志
        textv.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Debug: {msg}\n')
    elif level == 1:  # Trace级别日志
        textv.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Trace: {msg}\n')
    elif level == 2:  # Info级别日志
        textv.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Info: {msg}\n')
    elif level == 3:  # Warning级别日志
        textv.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Warning: {msg}\n')
    elif level == 4:  # Error级别日志
        textv.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Error: {msg}\n')
    else:
        raise ValueError("日志级别必须在0-4之间")