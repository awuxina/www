# send()和next效果一样,但能在上次yield那里传递一个值
def eater(name):
    print('{name} 开始吃东西了'.format(name=name))
    foods=[]
    while True:
        food = yield
        print('{name} 拿到{food},开始吃'.format(name=name, food=food))
        foods.append(food)
    print('结束')


e = eater('钢蛋')

next(e)
e.send('包子')
e.send('韭菜包子')
e.send('大蒜')
