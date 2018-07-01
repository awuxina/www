import abc
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def speak(self):
        pass
    @abc.abstractmethod
    def walk(self):
        pass


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

    def walk(self):
        print('猪快跑')
p = Pig()
p.run()
p.walk()
print(Pig.mro())
