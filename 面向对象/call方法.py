class People:
    def __init__(self,name):
        self.name=name

    def __call__(self, *args, **kwargs):
        print('call')
p=People('ecall')
p()
print(callable(p))


print(type(p))
print(type(People))
#typer---->类----->对象

