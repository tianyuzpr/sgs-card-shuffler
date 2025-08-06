import random
import utils
import os
import env

# 添加UI - 将所有UI创建代码移到mainloop之前
# utils.text = tk.Text(utils.window, wrap=tk.WORD, width=750, height=550)
# utils.text.pack(side=tk.RIGHT)

def env_init():
    if not os.path.exists(".env"):
        utils.Utils.log("ENV File not found", 1)
        utils.Utils.log("please set the ENV File", 1)
        sys.exit(1)
    import env
    return env

def shuffle_deck(print_func):
    global deck, discard_deck  # 声明deck和discard_deck为全局变量
    # 先将牌堆和弃牌堆合并
    deck.extend(discard_deck)
    discard_deck = []
    # 随机洗牌
    random.shuffle(deck)
    print_func(f"牌堆已重新洗牌，共有{len(deck)}张牌\n")

def card(deck_choice: int):
    global deck, discard_deck
    if deck_choice == 1:
        deck = sf_deck
    elif deck_choice == 2:
        deck = sfn_deck
    elif deck_choice == 3:
        deck = qz_deck + sf_deck
    elif deck_choice == 4:
        deck = qz_deck + sfn_deck
    elif deck_choice == 5:
        deck = gz_deck
    else:
        utils.Utils.log("无效的牌堆选项", 3)
        return
    utils.Utils.log("切换牌堆成功", 2)
    shuffle_deck(print)

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
    
    gz_deck = [
        "♡A桃园结义b", "♢A诸葛连弩(1)cW", "♧A白银狮子cF", "♤A闪电b$",
        "♡A万箭齐发b*", "♢A朱雀羽扇(4)cW", "♧A决斗b*", "♤A决斗b*",
        "♡2火攻b*", "♢2桃a", "♧2杀a", "♤2飞龙夺凤(2)cW",
        "♡2闪a", "♢2闪a", "♧2藤甲cF", "♤2八卦阵cF",
        "♡3火攻b*", "♢3闪a", "♧3知己知彼b", "♤3顺手牵羊b",
        "♡3五谷丰登b", "♢3顺手牵羊b", "♧3杀a", "♤3过河拆桥b",
        "♡4火杀a", "♢4火杀a", "♧4知己知彼b", "♤4顺手牵羊b",
        "♡4桃a", "♢4以逸待劳b", "♧4杀a", "♤4过河拆桥b",
        "♡5赤兔(-1)cZ-", "♢5火杀a", "♧5的卢(+1)cZ+", "♤5绝影(+1)cZ+",
        "♡5麒麟弓(5)cW", "♢5贯石斧", "♧5杀a", "♤5杀a",
        "♡6桃a", "♢6吴六剑(2)cW", "♧6雷杀a", "♤6雷杀a",
        "♡6乐不思蜀b$", "♢6闪a", "♧6乐不思蜀b$", "♤6青釭剑(2)cW",
        "♡7桃a", "♢7闪a", "♧7雷杀a", "♤7雷杀a",
        "♡7无中生有b", "♢7闪a", "♧7南蛮入侵b*", "♤7杀a",
        "♡8桃a", "♢8闪a", "♧8雷杀a", "♤8杀a",
        "♡8无中生有b", "♢8闪a", "♧8杀a", "♤8杀a",
        "♡9桃a", "♢9闪a", "♧9杀a", "♤9杀a",
        "♡9远交近攻b", "♢9酒a", "♧9酒a", "♤9酒a",
        "♡10桃a", "♢10杀a", "♧10杀a", "♤10杀a",
        "♡10杀a", "♢10闪a", "♧10兵粮寸断b$", "♤10兵粮寸断b$",
        "♡J闪a", "♢J闪a", "♧J杀a", "♤J杀a",
        "♡J以逸待劳b", "♢J杀a", "♧J杀a", "♤J无懈可击b",
        "♡Q桃b", "♢Q杀a", "♧Q借刀杀人b", "♤Q丈八蛇矛(3)cW",
        "♡Q过河拆桥b", "♢Q三尖两刃刀(3)cW", "♧Q铁索连环b", "♤Q铁索连环b",
        "♡K闪b", "♢K闪a", "♧K铁索连环b", "♤K南蛮入侵b*",
        "♡K爪黄飞电(+1)cZ+", "♢K紫骍(-1)cZ-", "♧K无懈可击·国b", "♤K大宛(-1)cZ-",
        "♡Q杀b", "♢Q无懈可击·国b", "♧2仁王盾cF", "♤2寒冰剑(2)cW",
        "♡3太平要术cF", "♢6定澜夜明珠cB", "♡K六龙骖驾(+1-1)cZ+cZ-",
        "♡A联军盛宴b", "♢A挟天子以令诸侯(合)b", "♧A玉玺cB", "♤A挟天子以令诸侯(合)b",
        "♡2调虎离山b", "♢2桃a", "♧2护心镜(合)cF?", "♤2明光铠cF",
        "♡3惊帆(-1)(合)cZ-", "♢3桃(合)a", "♧3敕令b", "♤3火烧连营(合)b*",
        "♡4闪a", "♢4挟天子以令诸侯(合)b", "♧4杀a", "♤4杀a",
        "♡5闪a", "♢5木牛流马cB", "♧5雷杀(合)a", "♤5青龙偃月刀(3)cW",
        "♡6闪(合)a", "♢6闪a", "♧6杀a", "♤6酒(合)a",
        "♡7闪a", "♢7闪a", "♧7杀a", "♤7杀a",
        "♡8桃a", "♢8火杀a", "♧8杀a", "♤8杀a",
        "♡9桃a", "♢9火杀a", "♧9酒a", "♤9雷杀a",
        "♡10桃a", "♢10杀a", "♧10杀a", "♤10杀a",
        "♡10杀a", "♢10闪a", "♧10兵粮寸断b$", "♤10兵粮寸断b$",
        "♡J杀a", "♢J无懈可击·国b", "♧J火烧连营(合)b*", "♤J雷杀(合)a",
        "♡Q火烧连营(合)b*", "♢Q方天画戟(4)cW", "♧Q水淹七军b*", "♤Q戮力同心b",
        "♡K水淹七军b*", "♢K闪a", "♧K无懈可击·国b", "♤K无懈可击b"
    ]
    
    deck = sf_deck  # 默认使用身份牌堆
    discard_deck = []
    
    # 检查牌堆数量是否正确
    if len(deck) != 160:
        utils.Utils.log("牌堆数量错误", 3)
    
    # 随机洗牌
    random.shuffle(deck)

def draw_card(num_cards, print_func):
    global deck, discard_deck  # 声明deck和discard_deck为全局变量
    int(num_cards)
    if num_cards <= 0:
        print_func("请输入一个正整数。\n")
        return
    if num_cards > len(deck):
        print_func(f"牌堆中只有{len(deck)}张牌，无法抽取{num_cards}张。\n")
        print_func(f"即将洗牌。\n")
        shuffle_deck(print_func)
        
    print_func(f"\n抽取前{num_cards}张牌：\n")
    for i in range(num_cards):
        print_func(deck[i] + '\n')
    # 进入弃牌堆
    discard_deck.extend(deck[:num_cards])
    deck = deck[num_cards:]
    print_func(f"\n已从牌堆中移除这{num_cards}张牌，剩余{len(deck)}张牌。\n")

def show_card(num_cards, print_func):
    global deck, discard_deck  # 声明deck和discard_deck为全局变量
    int(num_cards)
    if num_cards <= 0:
        print_func("请输入一个正整数。\n")
        return
    if num_cards > len(deck):
        print_func(f"牌堆中只有{len(deck)}张牌，无法展示{num_cards}张。\n")
        return
    print_func(f"\n展示牌堆中前{num_cards}张牌：\n")
    for i in range(num_cards):
        print_func(deck[i] + '\n')

if __name__ == "app":
    initialize_deck()