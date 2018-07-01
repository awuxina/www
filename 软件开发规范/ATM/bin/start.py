import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取根目录
sys.path.append(BASE_DIR)#将根目录加载到系统配置
# print('file==',__file__)
# print('os.path.abspath==',os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))

from core import test_main

if __name__== '__main__':#启动核心代码模块
    test_main.run()