<<<<<<< HEAD
import random
import tkinter as tk
from datetime import datetime
import builtins as bu
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
by tianyuzpr 2025-08-02
"""

# 定义全局变量
deck = []
discard_deck = []
text = None  # 用于存储Text控件的引用

def root():
    global text  # 声明text为全局变量
    
    window = tk.Tk()
    window.title("三国杀牌堆管理程序")
    window.geometry("800x600")
    
    # 添加UI - 将所有UI创建代码移到mainloop之前
    frame = tk.Frame(window)
    frame.pack()
    
    # 定义print函数
    _print_ = bu.print
    def print(msg: str, **kwargs):
        '''
        修改后的 `print()` 函数
        原: `_print_()` 
        '''
        msg = str(msg).replace('\u200b', '')
        try:
            text.insert(tk.END, msg + '\n')
        except Exception as e:
            _print_(f"print函数异常: {e}", file=sys.stderr)
    
    # 定义input函数,改为tk输入弹窗
    _input_ = bu.input
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
                return ""
        except Exception as e:
            _print_(f"input函数异常: {e}", file=sys.stderr)
            return ""
    
    # 创建菜单并配置到窗口上
    menu = tk.Menu(window)  # 创建菜单，绑定到窗口
    window.config(menu=menu)  # 将菜单配置到窗口上
    
    # 定义菜单
    card_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="牌操作", menu=card_menu)
    card_menu.add_command(label="抽取牌", command=lambda: draw_card(input("请输入抽取牌的数量:", "int")))   # 通过弹窗输入
    card_menu.add_command(label="展示牌", command=lambda: show_card(input("请输入展示牌的数量:", "int")))  # 通过弹窗输入
    card_menu.add_command(label="重新洗牌", command=shuffle_deck)
    card_menu.add_separator()
    card_menu.add_command(label="退出", command=window.destroy)
    
    # 右半部分输出，通过修改后的print
    text = tk.Text(frame, wrap=tk.WORD, width=750, height=550)
    text.pack(side=tk.RIGHT)
    

    # 将mainloop移到所有UI创建完成后
    window.mainloop()

def log(msg: str, level: int):
    '''
    自定义日志函数
    '''
    if level == 0:  # Debug级别日志
        text.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Debug: {msg}\n')
    elif level == 1:  # Trace级别日志
        text.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Trace: {msg}\n')
    elif level == 2:  # Info级别日志
        text.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Info: {msg}\n')
    elif level == 3:  # Warning级别日志
        text.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Warning: {msg}\n')
    elif level == 4:  # Error级别日志
        text.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Error: {msg}\n')
    else:
        raise ValueError("日志级别必须在0-4之间")

def initialize_deck():
    global deck, discard_deck
    deck = [
        "♡A桃园结义b", "♡A万箭齐发b*", "♡A无懈可击b", "♡2闪a", "♡2闪a", "♡2火攻b*", "♡3桃a", "♡3五谷丰登b", "♡3火攻b*",
        "♡4桃a", "♡4五谷丰登b", "♡4火杀a", "♡5赤兔(-1)cZ-", "♡5麒麟弓(5)cW", "♡5桃a", "♡6桃a", "♡6乐不思蜀b$", "♡6桃a",
        "♡7桃a", "♡7无中生有b", "♡7火杀a", "♡8桃a", "♡8无中生有b", "♡8闪a", "♡9桃a", "♡9无中生有b", "♡9闪a",
        "♡10杀a", "♡10杀a", "♡10火杀a", "♡J杀a", "♡J无中生有b", "♡J闪a",
        "♡Q桃a", "♡Q过河拆桥b", "♡Q闪a", "♡Q闪电b$", "♡K闪a", "♡K爪黄飞电(+1)cZ+", "♡K无懈可击b",
        
        "♢A诸葛连弩(1)cW", "♢A决斗b*", "♢A朱雀羽扇(4)cW", "♢2闪a", "♢2闪a", "♢2桃a", "♢3闪a", "♢3顺手牵羊b", "♢3桃a",
        "♢4闪a", "♢4顺手牵羊b", "♢4火杀a", "♢5闪a", "♢5贯石斧(3)cW", "♢5火杀a", "♢6杀a", "♢6闪a", "♢6闪a",
        "♢7杀a", "♢7闪a", "♢7闪a", "♢8杀a", "♢8闪a", "♢8闪a", "♢9杀a", "♢9闪a", "♢9酒a",
        "♢10杀a", "♢10闪a", "♢10闪a", "♢J闪a", "♢J闪a", "♢J闪a",
        "♢Q桃a", "♢Q方天画戟(4)cW", "♢Q火攻b*", "♢Q无懈可击b", "♢K杀a", "♢K紫骍(-1)cZ-", "♢K骅骝(+1)cZ+",
        
        "♧A诸葛连弩(1)cW", "♧A决斗b*", "♧A白银狮子cF", "♧2杀a", "♧2八卦阵cF", "♧2藤甲cF", "♧2仁王盾cF", "♧3杀a", "♧3过河拆桥b", "♧3酒a",
        "♧4杀a", "♧4过河拆桥b", "♧4兵粮寸断b$", "♧5的卢(+1)cZ+", "♧5杀a", "♧5雷杀a", "♧6杀a", "♧6乐不思蜀b$", "♧6雷杀a",
        "♧7杀a", "♧7南蛮入侵b*", "♧7雷杀a", "♧8杀a", "♧8杀a", "♧8雷杀a", "♧9杀a", "♧9杀a", "♧9酒a",
        "♧10杀a", "♧10杀a", "♧10铁索连环b", "♧J杀a", "♧J杀a", "♧J铁索连环b",
        "♧Q借刀杀人b", "♧Q无懈可击b", "♧Q铁索连环b", "♧K借刀杀人b", "♧K无懈可击b", "♧K铁索连环b",
        
        "♤A闪电b$", "♤A决斗b*", "♤A古锭刀(2)cW", "♤2雌雄双股剑(2)cW", "♤2八卦阵cF", "♤2藤甲cF", "♤2寒冰剑(2)cW", "♤3顺手牵羊b", "♤3过河拆桥b", "♤3酒a",
        "♤4顺手牵羊b", "♤4过河拆桥b", "♤4雷杀a", "♤5绝影(+1)cZ+", "♤5青龙偃月刀(3)cW", "♤5雷杀a", "♤6青釭剑(2)cW", "♤6乐不思蜀b$", "♤6雷杀a",
        "♤7杀a", "♤7南蛮入侵b*", "♤7雷杀a", "♤8杀a", "♤8杀a", "♤8雷杀a", "♤9杀a", "♤9杀a", "♤9酒a",
        "♤10杀a", "♤10杀a", "♤10兵粮寸断b$", "♤J顺手牵羊b", "♤J无懈可击b", "♤J铁索连环b",
        "♤Q丈八蛇矛(3)cW", "♤Q过河拆桥b", "♤Q铁索连环b", "♤K南蛮入侵b*", "♤K大宛(-1)cZ-", "♤K无懈可击b"
    ]
    
    discard_deck = []
    
    # 检查牌堆数量是否正确
    if len(deck) != 160:
        log("牌堆数量错误", 3)
    
    # 随机洗牌
    shuffle_deck()

def shuffle_deck():
    global deck
    random.shuffle(deck)
    text.insert(tk.END, f"牌堆已重新洗牌，共有{len(deck)}张牌\n")

def draw_card(num_cards):
    global deck, discard_deck
    if num_cards <= 0:
        text.insert(tk.END, "请输入一个正整数。\n")
        return
    if num_cards > len(deck):
        text.insert(tk.END, f"牌堆中只有{len(deck)}张牌，无法抽取{num_cards}张。\n")
        return
    text.insert(tk.END, f"\n抽取前{num_cards}张牌：\n")
    for i in range(num_cards):
        text.insert(tk.END, deck[i] + '\n')
    # 进入弃牌堆
    discard_deck.extend(deck[:num_cards])
    deck = deck[num_cards:]
    text.insert(tk.END, f"\n已从牌堆中移除这{num_cards}张牌，剩余{len(deck)}张牌。\n")

def show_card(num_cards):
    global deck
    if num_cards <= 0:
        text.insert(tk.END, "请输入一个正整数。\n")
        return
    if num_cards > len(deck):
        text.insert(tk.END, f"牌堆中只有{len(deck)}张牌，无法展示{num_cards}张。\n")
        return
    text.insert(tk.END, f"\n展示{num_cards}张牌：\n")
    for i in range(num_cards):
        text.insert(tk.END, deck[i] + '\n')

if __name__ == "__main__":
    # 先创建root窗口初始化text变量
    window = tk.Tk()
    window.withdraw()  # 隐藏主窗口
    text = tk.Text(window)
    
    initialize_deck()
    root()
=======
import random
import tkinter as tk
from datetime import datetime
import builtins as bu
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
by tianyuzpr 2025-08-02
"""

# 定义全局变量
deck = []
discard_deck = []
text = None  # 用于存储Text控件的引用

def root():
    global text  # 声明text为全局变量
    
    window = tk.Tk()
    window.title("三国杀牌堆管理程序")
    window.geometry("800x600")
    
    # 添加UI - 将所有UI创建代码移到mainloop之前
    frame = tk.Frame(window)
    frame.pack()
    
    # 定义print函数
    _print_ = bu.print
    def print(msg: str, **kwargs):
        '''
        修改后的 `print()` 函数
        原: `_print_()` 
        '''
        msg = str(msg).replace('\u200b', '')
        try:
            text.insert(tk.END, msg + '\n')
        except Exception as e:
            _print_(f"print函数异常: {e}", file=sys.stderr)
    
    # 定义input函数,改为tk输入弹窗
    _input_ = bu.input
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
                return ""
        except Exception as e:
            _print_(f"input函数异常: {e}", file=sys.stderr)
            return ""
    
    # 创建菜单并配置到窗口上
    menu = tk.Menu(window)  # 创建菜单，绑定到窗口
    window.config(menu=menu)  # 将菜单配置到窗口上
    
    # 定义菜单
    card_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="牌操作", menu=card_menu)
    card_menu.add_command(label="抽取牌", command=lambda: draw_card(input("请输入抽取牌的数量:", "int")))   # 通过弹窗输入
    card_menu.add_command(label="展示牌", command=lambda: show_card(input("请输入展示牌的数量:", "int")))  # 通过弹窗输入
    card_menu.add_command(label="重新洗牌", command=shuffle_deck)
    card_menu.add_separator()
    card_menu.add_command(label="退出", command=window.destroy)
    
    # 右半部分输出，通过修改后的print
    text = tk.Text(frame, wrap=tk.WORD, width=750, height=550)
    text.pack(side=tk.RIGHT)
    

    # 将mainloop移到所有UI创建完成后
    window.mainloop()

def log(msg: str, level: int):
    '''
    自定义日志函数
    '''
    if level == 0:  # Debug级别日志
        text.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Debug: {msg}\n')
    elif level == 1:  # Trace级别日志
        text.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Trace: {msg}\n')
    elif level == 2:  # Info级别日志
        text.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Info: {msg}\n')
    elif level == 3:  # Warning级别日志
        text.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Warning: {msg}\n')
    elif level == 4:  # Error级别日志
        text.insert(tk.END, f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Error: {msg}\n')
    else:
        raise ValueError("日志级别必须在0-4之间")

def initialize_deck():
    global deck, discard_deck
    deck = [
        "♡A桃园结义b", "♡A万箭齐发b*", "♡A无懈可击b", "♡2闪a", "♡2闪a", "♡2火攻b*", "♡3桃a", "♡3五谷丰登b", "♡3火攻b*",
        "♡4桃a", "♡4五谷丰登b", "♡4火杀a", "♡5赤兔(-1)cZ-", "♡5麒麟弓(5)cW", "♡5桃a", "♡6桃a", "♡6乐不思蜀b$", "♡6桃a",
        "♡7桃a", "♡7无中生有b", "♡7火杀a", "♡8桃a", "♡8无中生有b", "♡8闪a", "♡9桃a", "♡9无中生有b", "♡9闪a",
        "♡10杀a", "♡10杀a", "♡10火杀a", "♡J杀a", "♡J无中生有b", "♡J闪a",
        "♡Q桃a", "♡Q过河拆桥b", "♡Q闪a", "♡Q闪电b$", "♡K闪a", "♡K爪黄飞电(+1)cZ+", "♡K无懈可击b",
        
        "♢A诸葛连弩(1)cW", "♢A决斗b*", "♢A朱雀羽扇(4)cW", "♢2闪a", "♢2闪a", "♢2桃a", "♢3闪a", "♢3顺手牵羊b", "♢3桃a",
        "♢4闪a", "♢4顺手牵羊b", "♢4火杀a", "♢5闪a", "♢5贯石斧(3)cW", "♢5火杀a", "♢6杀a", "♢6闪a", "♢6闪a",
        "♢7杀a", "♢7闪a", "♢7闪a", "♢8杀a", "♢8闪a", "♢8闪a", "♢9杀a", "♢9闪a", "♢9酒a",
        "♢10杀a", "♢10闪a", "♢10闪a", "♢J闪a", "♢J闪a", "♢J闪a",
        "♢Q桃a", "♢Q方天画戟(4)cW", "♢Q火攻b*", "♢Q无懈可击b", "♢K杀a", "♢K紫骍(-1)cZ-", "♢K骅骝(+1)cZ+",
        
        "♧A诸葛连弩(1)cW", "♧A决斗b*", "♧A白银狮子cF", "♧2杀a", "♧2八卦阵cF", "♧2藤甲cF", "♧2仁王盾cF", "♧3杀a", "♧3过河拆桥b", "♧3酒a",
        "♧4杀a", "♧4过河拆桥b", "♧4兵粮寸断b$", "♧5的卢(+1)cZ+", "♧5杀a", "♧5雷杀a", "♧6杀a", "♧6乐不思蜀b$", "♧6雷杀a",
        "♧7杀a", "♧7南蛮入侵b*", "♧7雷杀a", "♧8杀a", "♧8杀a", "♧8雷杀a", "♧9杀a", "♧9杀a", "♧9酒a",
        "♧10杀a", "♧10杀a", "♧10铁索连环b", "♧J杀a", "♧J杀a", "♧J铁索连环b",
        "♧Q借刀杀人b", "♧Q无懈可击b", "♧Q铁索连环b", "♧K借刀杀人b", "♧K无懈可击b", "♧K铁索连环b",
        
        "♤A闪电b$", "♤A决斗b*", "♤A古锭刀(2)cW", "♤2雌雄双股剑(2)cW", "♤2八卦阵cF", "♤2藤甲cF", "♤2寒冰剑(2)cW", "♤3顺手牵羊b", "♤3过河拆桥b", "♤3酒a",
        "♤4顺手牵羊b", "♤4过河拆桥b", "♤4雷杀a", "♤5绝影(+1)cZ+", "♤5青龙偃月刀(3)cW", "♤5雷杀a", "♤6青釭剑(2)cW", "♤6乐不思蜀b$", "♤6雷杀a",
        "♤7杀a", "♤7南蛮入侵b*", "♤7雷杀a", "♤8杀a", "♤8杀a", "♤8雷杀a", "♤9杀a", "♤9杀a", "♤9酒a",
        "♤10杀a", "♤10杀a", "♤10兵粮寸断b$", "♤J顺手牵羊b", "♤J无懈可击b", "♤J铁索连环b",
        "♤Q丈八蛇矛(3)cW", "♤Q过河拆桥b", "♤Q铁索连环b", "♤K南蛮入侵b*", "♤K大宛(-1)cZ-", "♤K无懈可击b"
    ]
    
    discard_deck = []
    
    # 检查牌堆数量是否正确
    if len(deck) != 160:
        log("牌堆数量错误", 3)
    
    # 随机洗牌
    shuffle_deck()

def shuffle_deck():
    global deck
    random.shuffle(deck)
    text.insert(tk.END, f"牌堆已重新洗牌，共有{len(deck)}张牌\n")

def draw_card(num_cards):
    global deck, discard_deck
    if num_cards <= 0:
        text.insert(tk.END, "请输入一个正整数。\n")
        return
    if num_cards > len(deck):
        text.insert(tk.END, f"牌堆中只有{len(deck)}张牌，无法抽取{num_cards}张。\n")
        return
    text.insert(tk.END, f"\n抽取前{num_cards}张牌：\n")
    for i in range(num_cards):
        text.insert(tk.END, deck[i] + '\n')
    # 进入弃牌堆
    discard_deck.extend(deck[:num_cards])
    deck = deck[num_cards:]
    text.insert(tk.END, f"\n已从牌堆中移除这{num_cards}张牌，剩余{len(deck)}张牌。\n")

def show_card(num_cards):
    global deck
    if num_cards <= 0:
        text.insert(tk.END, "请输入一个正整数。\n")
        return
    if num_cards > len(deck):
        text.insert(tk.END, f"牌堆中只有{len(deck)}张牌，无法展示{num_cards}张。\n")
        return
    text.insert(tk.END, f"\n展示{num_cards}张牌：\n")
    for i in range(num_cards):
        text.insert(tk.END, deck[i] + '\n')

if __name__ == "__main__":
    # 先创建root窗口初始化text变量
    window = tk.Tk()
    window.withdraw()  # 隐藏主窗口
    text = tk.Text(window)
    
    initialize_deck()
    root()
>>>>>>> 666736a8d5d4c3c2dab24db3507618e843e6c261
    window.destroy()