# app.py
import tkinter as tk
import random
import utils
import sys
from tkinter import simpledialog

# 添加UI - 将所有UI创建代码移到mainloop之前
utils.text = tk.Text(utils.window, wrap=tk.WORD, width=750, height=550)
utils.text.pack(side=tk.RIGHT)

def shuffle_deck(text):
    global deck, discard_deck  # 声明deck和discard_deck为全局变量
    # 先将牌堆和弃牌堆合并
    deck.extend(discard_deck)
    discard_deck = []
    # 随机洗牌
    random.shuffle(deck)
    text.insert(tk.END, f"牌堆已重新洗牌，共有{len(deck)}张牌\n")

def card(kazu: str):
    global deck, discard_deck
    if kazu == "sf":
        deck = sf_deck
    elif kazu == "sfn":
        deck = sfn_deck
    elif kazu == "gz":
        deck = gz_deck
    elif kazu == "qz":
        deck = sf_deck + qz_deck
    elif kazu == "qzn":
        deck = sfn_deck + qz_deck
    else:
        utils.log("牌堆不存在", 3)
        return
    utils.log("切换牌堆成功", 2)
    shuffle_deck(utils.text)

def initialize_deck():
    global sf_deck, sfn_deck, gz_deck, qz_deck, discard_deck, deck
    
    sf_deck = [
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
    
    sfn_deck = [
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
        "♤Q丈八蛇矛(3)cW", "♤Q过河拆桥b", "♤Q铁索连环b", "♤K南蛮入侵b*", "♤K大宛(-1)cZ-", "♤K无懈可击b",
        
        "♢5木牛流马cB"
    ]
    
    qz_deck = ["♤2奇正相生b", "♤4奇正相生b", "♤6奇正相生b", "♤8奇正相生b", "♧3奇正相生b", "♧5奇正相生b", "♧7奇正相生b", "♧9奇正相生b"]
    
    gz_deck = []
    
    deck = sf_deck # 默认是身份局
    
    discard_deck = []
    
    # 检查牌堆数量是否正确
    if len(deck) != 160:
        utils.log("牌堆数量错误", 3)
    
    # 随机洗牌
    random.shuffle(deck)

def draw_card(num_cards, text):
    global deck, discard_deck  # 声明deck和discard_deck为全局变量
    int(num_cards)
    if num_cards <= 0:
        text.insert(tk.END, "请输入一个正整数。\n")
        return
    if num_cards > len(deck):
        text.insert(tk.END, f"牌堆中只有{len(deck)}张牌，无法抽取{num_cards}张。\n")
        text.insert(tk.END, f"即将洗牌。\n")
        shuffle_deck(text)
        
    text.insert(tk.END, f"\n抽取前{num_cards}张牌：\n")
    for i in range(num_cards):
        text.insert(tk.END, deck[i] + '\n')
    # 进入弃牌堆
    discard_deck.extend(deck[:num_cards])
    deck = deck[num_cards:]
    text.insert(tk.END, f"\n已从牌堆中移除这{num_cards}张牌，剩余{len(deck)}张牌。\n")

def show_card(num_cards, text):
    global deck, discard_deck  # 声明deck和discard_deck为全局变量
    int(num_cards)
    if num_cards <= 0:
        text.insert(tk.END, "请输入一个正整数。\n")
        return
    if num_cards > len(deck):
        text.insert(tk.END, f"牌堆中只有{len(deck)}张牌，无法展示{num_cards}张。\n")
        return
    text.insert(tk.END, f"\n展示牌堆中前{num_cards}张牌：\n")
    for i in range(num_cards):
        text.insert(tk.END, deck[i] + '\n')

if __name__ == "app":
    initialize_deck()