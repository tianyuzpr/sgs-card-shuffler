from datetime import datetime
import random

class Utils:
    @staticmethod
    def log(msg: str, level: int):
        '''
        自定义日志函数
        '''
        if level == 0:  # Debug级别日志
            print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Debug: {msg}')
        elif level == 1:  # Trace级别日志
            print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Trace: {msg}')
        elif level == 2:  # Info级别日志
            print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Info: {msg}')
        elif level == 3:  # Warning级别日志
            print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Warning: {msg}')
        elif level == 4:  # Error级别日志
            print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Error: {msg}')
        else:
            raise ValueError("日志级别必须在0-4之间")

    @staticmethod
    def shuffle_deck(deck, discard_deck):
        '''
        洗牌逻辑
        '''
        deck.extend(discard_deck)
        discard_deck.clear()
        random.shuffle(deck)
        Utils.log(f"牌堆已重新洗牌，共有{len(deck)}张牌", 2)

    @staticmethod
    def draw_card(num_cards, deck, discard_deck):
        '''
        抽牌逻辑
        '''
        if num_cards <= 0:
            Utils.log("请输入一个正整数。", 3)
            return "请输入一个正整数。"
        if num_cards > len(deck):
            Utils.log(f"牌堆中只有{len(deck)}张牌，无法抽取{num_cards}张。", 3)
            Utils.log("即将洗牌。", 2)
            Utils.shuffle_deck(deck, discard_deck)
        
        drawn_cards = deck[:num_cards]
        discard_deck.extend(drawn_cards)
        del deck[:num_cards]
        Utils.log(f"抽取前{num_cards}张牌：", 2)
        for card in drawn_cards:
            Utils.log(card, 2)
        Utils.log(f"已从牌堆中移除这{num_cards}张牌，剩余{len(deck)}张牌。", 2)
        return drawn_cards

    @staticmethod
    def show_card(num_cards, deck):
        '''
        展示牌逻辑
        '''
        if num_cards <= 0:
            Utils.log("请输入一个正整数。", 3)
            return "请输入一个正整数。"
        if num_cards > len(deck):
            Utils.log(f"牌堆中只有{len(deck)}张牌，无法展示{num_cards}张。", 3)
            return f"牌堆中只有{len(deck)}张牌，无法展示{num_cards}张。"
        Utils.log(f"展示牌堆中前{num_cards}张牌：", 2)
        shown_cards = deck[:num_cards]
        for card in shown_cards:
            Utils.log(card, 2)
        return shown_cards