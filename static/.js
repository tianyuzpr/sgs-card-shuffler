$(document).ready(function() {
    // 洗牌按钮点击事件
    $('#shuffle').click(function() {
        $.post('/shuffle', function(data) {
            $('#output').text('牌堆已重新洗牌');
        });
    });

    // 抽牌按钮点击事件
    $('#draw').click(function() {
        let num_cards = prompt('请输入抽取牌的数量:');
        if (num_cards && !isNaN(num_cards) && parseInt(num_cards) > 0) {
            $.post('/draw', { num_cards: num_cards }, function(data) {
                if (data && data.length > 0) {
                    $('#output').text('抽取的牌: ' + data.join(', '));
                } else {
                    $('#output').text('没有抽取到牌，请检查牌堆数量或重新洗牌');
                }
            });
        } else {
            alert('请输入一个有效的正整数！');
        }
    });

    // 展示牌按钮点击事件
    $('#show').click(function() {
        let num_cards = prompt('请输入展示牌的数量:');
        if (num_cards && !isNaN(num_cards) && parseInt(num_cards) > 0) {
            $.post('/show', { num_cards: num_cards }, function(data) {
                if (data && data.length > 0) {
                    $('#output').text('展示的牌: ' + data.join(', '));
                } else {
                    $('#output').text('没有展示到牌，请检查牌堆数量');
                }
            });
        } else {
            alert('请输入一个有效的正整数！');
        }
    });

    // 切换牌堆按钮点击事件
    $('#change_deck').click(function() {
    let deck_type = $('#deck_options').val();
    if (deck_type && ['sf', 'sfn', 'gz', 'qz', 'qzn'].includes(deck_type.toLowerCase())) {
        $.post('/change_deck', { deck_type: deck_type }, function(data) {
            $('#output_text').val($('#output_text').val() + '\n牌堆已切换');
        });
    } else {
        alert('无效的牌堆类型，请选择正确的类型！');
    }
});
});
