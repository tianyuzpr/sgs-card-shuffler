from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import utils
from app import sf_deck, sfn_deck, gz_deck, qz_deck, discard_deck



app = Flask(__name__)

# 初始化牌堆
app.deck = sf_deck
app.discard_deck = discard_deck

@app.route('/')
def index():
    return render_template('index.html')  # 确保 index.html 在 templates 文件夹中

@app.route('/shuffle', methods=['POST'])
def shuffle():
    utils.Utils.shuffle_deck(app.deck, app.discard_deck)
    return redirect(url_for('index'))

@app.route('/draw', methods=['POST'])
def draw():
    num_cards = int(request.form['num_cards'])
    drawn_cards = utils.Utils.draw_card(num_cards, app.deck, app.discard_deck)
    return jsonify(drawn_cards)

@app.route('/show', methods=['POST'])
def show():
    num_cards = int(request.form['num_cards'])
    shown_cards = utils.Utils.show_card(num_cards, app.deck)
    return jsonify(shown_cards)

@app.route('/change_deck', methods=['POST'])
def change_deck():
    deck_type = request.form['deck_type']
    if deck_type == 'sf':
        app.deck = sf_deck
    elif deck_type == 'sfn':
        app.deck = sfn_deck
    elif deck_type == 'gz':
        app.deck = gz_deck
    elif deck_type == 'qz':
        app.deck = qz_deck
    elif deck_type == 'qzn':
        app.deck = qz_deck + sfn_deck
    return jsonify({"message": "牌堆已切换"})
if __name__ == '__main__':
    port = int(os.getenv('tcp', 23333))  # 从环境变量中获取端口号，默认为23333
    app.run(host='0.0.0.0', port=port)