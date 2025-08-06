import random
from datetime import datetime
import builtins as bu
import sys
from app import *
import utils
import env

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

# 检查env
if not os.path.exists("env.env"):
    utils.log("ENV File not found", 1)
    utils.log("please set the ENV File", 1)
    sys.exit(1)

def env():
    import env
    # 导入env.env
    env.load_env()
    return env

# 定义print函数
_print_ = print
def print(msg: str, **kwargs):
    '''
    修改后的 `print()` 函数
    原: `_print_()` 
    '''
    msg = str(msg).replace('\u200b', '')
    try:
        _print_(msg, **kwargs)
    except Exception as e:
        _print_(f"print函数异常: {e}", file=sys.stderr)
    
# 定义input函数
_input_ = input
def input(prompt: str = "", type: str = "str") -> str:
    '''
    修改后的 `input()` 函数
    原: `_input_()` 
    '''
    try:
        if type == "int":
            return int(_input_(prompt))
        elif type == "float":
            return float(_input_(prompt))
        elif type == "bool":
            return _input_(prompt).lower() in ["yes", "y", "true"]
        elif type == "str":
            return _input_(prompt)
        else:
            _print_("input函数异常: type参数错误", file=sys.stderr)
            return None
    except Exception as e:
        _print_(f"input函数异常: {e}", file=sys.stderr)
    return None

def main():
    # 初始化牌堆
    initialize_deck()

    while True:
        print("\n请选择操作：")
        print("1. 抽取牌")
        print("2. 展示牌")
        print("3. 重新洗牌")
        print("4. 切换牌堆")
        print("5. 退出")
        choice = input("请输入选项编号：", "int")
        
        if choice == 1:
            num_cards = input("请输入抽取牌的数量:", "int")
            draw_card(num_cards, print)
        elif choice == 2:
            num_cards = input("请输入展示牌的数量:", "int")
            show_card(num_cards, print)
        elif choice == 3:
            shuffle_deck(print)
        elif choice == 4:
            print("\n请选择牌堆类型：")
            print("1. sf - 身份牌堆")
            print("2. sfn - 身份牌堆（有木牛）")
            print("3. qz - 神荀彧牌堆")
            print("4. qzn - 神荀彧牌堆（有木牛）")
            print("5. gz - 国战牌堆")
            deck_choice = input("请输入选项编号：", "int")
            if deck_choice == 1:
                card(1)
            elif deck_choice == 2:
                card(2)
            elif deck_choice == 3:
                card(3)
            elif deck_choice == 4:
                card(4)
            elif deck_choice == 5:
                card(5)
            else:
                print("无效的选项，请重新输入。")
        elif choice == 5:
            print("程序已退出。")
            break
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    # 启动主程序
    main()