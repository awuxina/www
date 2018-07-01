menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

# last_layer = menu #上一层
# current_layer = menu #当前层
#
# while True:
#     for key in current_layer:
#         print(key)
#     choice = input('>>:').strip()
#     if len(choice)==0:
#         continue
#
#     if choice in current_layer: #如果输入
#         last_layer = current_layer
#         current_layer = current_layer[choice]
#         continue
#
#     if choice == 'b':
#         current_layer = last_layer


last_layers = [menu]  # 上一层
current_layer = menu  # 当前层

while True:
    for key in current_layer:
        print(key)
    choice = input('>>:').strip()
    if len(choice) == 0:
        continue

    if choice in current_layer:  # 如果输入
        last_layers.append(current_layer)  # 添加到列表
        current_layer = current_layer[choice]
        continue

    if choice == 'b':
        if len(last_layers) == 1:
            continue
        current_layer = last_layers[-1]  # 取到上一层,赋值给当前层
        last_layers.pop()  # 删除下一层
    elif choice == 'q':
        break
