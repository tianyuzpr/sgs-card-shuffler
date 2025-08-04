import random
import tkinter as tk
from datetime import datetime
import builtins as bu
from app import *
import utils
import sys
from tkinter import simpledialog

"""
开始之前先叠个藤甲（不是）
这段代码的自定义print和input灵感来源于另一位大佬：@wyf9
自定义print和input的原因是为了在tkinter窗口中显示输出和输入，而不是在控制台中。但是有一些问题，解决欢迎提pr
另外，tkinter的输入弹窗只能输入字符串，所以自定义input函数需要根据type参数来判断输入类型。
如果需要输出日志，我也做好了log()函数，你可以在需要输出日志的地方调用log()函数，而不是麻烦的手动
log使用说明
log(msg: str,level: int)
msg: 日志信息
level: 日志级别
0: Debug级别日志
1: Trace级别日志
2: Info级别日志
3: Warning级别日志
4: Error级别日志
如果有什么不懂的地方，或者有什么建议，欢迎提issue。
by @CR400AF-C-2214 2025-08-02
"""

# 定义print函数
_print_ = print
def print(msg: str, **kwargs):
    '''
    修改后的 `print()` 函数
    原: `_print_()` 
    '''
    msg = str(msg).replace('\u200b', '')
    try:
        utils.text.insert(tk.END, msg + '\n')
    except Exception as e:
        _print_(f"print函数异常: {e}", file=sys.stderr)
    
# 定义input函数,改为tk输入弹窗
_input_ = input
def input(prompt: str = "", type: str = "str") -> str:
    '''
    修改后的 `input()` 函数
    原: `_input_()` 
    '''
    try:
        if type == "int":
            return tk.simpledialog.askinteger("输入", prompt)
        elif type == "float":
            return tk.simpledialog.askfloat("输入", prompt)
        elif type == "bool":
            return tk.simpledialog.askyesno("确认", prompt)
        elif type == "str":
            return tk.simpledialog.askstring("输入", prompt)
        else:
            _print_("input函数异常: type参数错误", file=sys.stderr)
            return None
    except Exception as e:
        _print_(f"input函数异常: {e}", file=sys.stderr)
    return None
def root():
    global text, window  # 声明全局变量
    utils.window = tk.Tk()
    utils.window.title("三国杀牌堆管理程序")
    utils.window.geometry("800x600")
    # 输出，通过修改后的print
    utils.text = tk.Text(utils.window, wrap=tk.WORD, width=750, height=550)
    utils.text.pack(side=tk.RIGHT)
    # 添加UI - 将所有UI创建代码移到mainloop之前
    frame = tk.Frame(utils.window)
    frame.pack()
    
    # 创建菜单并配置到窗口上
    menu = tk.Menu(utils.window)  # 创建菜单，绑定到窗口
    utils.window.config(menu=menu)  # 将菜单配置到窗口上
    
    # 初始化牌堆
    initialize_deck()

    # 定义菜单
    card_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="牌操作", menu=card_menu)
    card_menu.add_command(label="抽取牌", command=lambda: draw_card(input("请输入抽取牌的数量:", "int"), utils.text))   # 通过弹窗输入
    card_menu.add_command(label="展示牌", command=lambda: show_card(input("请输入展示牌的数量:", "int"), utils.text))  # 通过弹窗输入
    card_menu.add_command(label="重新洗牌", command=lambda: shuffle_deck(utils.text))
    card_menu.add_separator()
    card_menu.add_command(label="退出", command=utils.window.destroy)
    
    kazu_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="切换牌堆", menu=kazu_menu)
    kazu_menu.add_command(label="身份牌堆", command=lambda: card("sf"))
    kazu_menu.add_command(label="身份牌堆(有木牛)", command=lambda: card("sfn"))
    kazu_menu.add_command(label="国战牌堆", command=lambda: card("gz"))
    kazu_menu.add_command(label="神荀彧牌堆", command=lambda: card("qz"))
    kazu_menu.add_command(label="神荀彧牌堆(有木牛)", command=lambda: card("qzn"))
    # ————————————————
    utils.window.protocol('WM_DELETE_WINDOW', sys.exit)  # 点击X按钮时调用sys.exit()
    
    tk.messagebox.showwarning(title='提示', message='请关闭标题为tk的窗口')
    # 将mainloop移到所有UI创建完成后
    utils.window.mainloop()
    # —————————————————
    # 我甚至不知道这段代码是怎么跑起来的 @CR400AF-C-2214 25-8-3

if __name__ == "__main__":
    # 启动主界面
    root()
    exit()