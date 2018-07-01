class Animal:
    def run(self):
        pass
    def speak(self):
        pass
    def walk(self):
        raise AttributeError('子类必须实现这个方法')

class People(Animal):
    def run(self):
        print('人正在走')

    def speak(self):
        print('说话')

class Pig(Animal):
    def run(self):
        print('pig is walking')

    def speak(self):
        print('嗷嗷嗷')

p=Pig()
p.run()
p.walk()