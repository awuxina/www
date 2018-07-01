# #简单的序列化
# # d={'河北':['廊坊','保定'],'湖南':['长沙','韶山']}
# # s=str(d)
# # with open('data','w') as f:
# #     f.write(s)
#
# # with open('data') as f2:
# #     s2=f2.read()
# #     d2=eval(s2)
# # print(s)
# # print(d2['河北'])
# #简单的序列化 END
#
# import json
# d={'name':'egon'}
# #序列化 方法1
# s=json.dumps(d)#将字典d转为json字符串
# print(type(s))
# print(s)
# #写入文件
# # with open('data','w') as f:
# #     f.write(s)
# #写入文件   END
# #序列化 方法1   END
#
# #序列化 方法2
# # f=open('data','w')
# # json.dump(d,f)#将字典d转为json字符串,并写入文件
# # f.close()
# #序列化 方法2   END
#
# #反序列化
# #读取文件
# data=''
# with open('data') as f:
#     data=json.loads(f.read())#将字符串转化为字典
# #读取文件   END
# print(type(data))
# print(data)
# #反序列化
#
#
# i=10
# s='hello'
# t=(1,4,6)
# l=[3,5,7]
# d={'name':'yuan'}
# json_str1=json.dumps(i)
# json_str2=json.dumps(s)
# json_str3=json.dumps(t)
# json_str4=json.dumps(l)
# json_str5=json.dumps(d)
#
# print(json_str1)    #'10'
# print(json_str2)    #'"hello"'
# print(json_str3)    #'[1, 4, 6]'
# print(json_str4)    #'[3, 5, 7]'
# print(json_str5)    #'{"name": "yuan"}'


#------------------------------------------pickle-----------------------------------------------------
class Foo:
    def hello(self):
        pass

#pickle数据无法直接文件观看
#ouckle支持任何数据类型序列化,只能用于python平台交换数据
import pickle
#一般序列化
# d={'name':'alvin'}
d=Foo() #序列化任意类型
s=pickle.dumps(d)
print(s,type(s))
#序列化
with open('data_pickle','wb') as f:
    f.write(s)
#序列化 END

#反序列化   END
data=''
with open('data_pickle','rb') as f:
    data=pickle.loads(f.read())
#反序列化
print(data,type(data))
#一般序列化  END


