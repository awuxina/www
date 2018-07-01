#模块的查找顺序 内存:sys.modules->内建->最后找sys.path
import sys
print(sys.path)#模块查找顺序

#加载不在当前路径的模块
sys.path.append('D:\\python\\project\\面向对象')
import new
