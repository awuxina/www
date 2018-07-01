class A:
    def __enter__(self):
        print('开始')

    def __exit__(self, e_t, e_v, t_b):
        print('结束')

with A() as a:
    print('.....')