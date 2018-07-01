def order(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        next(res)
        return res
    return wrapper

@order
def eater(name):
    print('{name} 开始吃东西了'.format(name=name))
    foods = []
    while True:
        food = yield
        print('{name} 拿到{food},开始吃'.format(name=name, food=food))
        foods.append(food)
    print('结束')


e = eater('钢蛋')
e.send('包子')
e.send('包子')
e.send('韭菜包子')
e.send('大蒜')
