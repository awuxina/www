# 1、使用while循环输入 1 2 3 ... 8 9 10
# i=1
# while i<11:
#     print(i)
#     i+=1
# 1、使用while循环输入 1 2 3 ... 8 9 10 END

# 2、求1-100的所有数的和
# i=1
# result=0
# while i<101:
#     result =result+i
#     i+=1
# print(result)
# 2、求1-100的所有数的和 END

# 3、输出 1-100 内的所有奇数
# i=1
# result=0
# while i<101:
#     if i%2==1:
#         print(i)
#     i += 1
# #3、输出 1-100 内的所有奇数  END

# 4、输出 1-100 内的所有偶数
# i=1
# result=0
# while i<101:
#     if i%2==0:
#         print(i)
#     i += 1
# #4、输出 1-100 内的所有偶数  END

# 5、求1-2+3-4 ... 99的所有数的和
# i = 1
# result = 0
# while i < 101:
#     if i % 2 == 1:
#         result = result + i
#     if i % 2 == 0:
#         result = result - i
#     i += 1
# print(result)
# 5、求1-2+3-4 ... 99的所有数的和    END

#模拟登陆
    # 1. 用户输入帐号密码进行登陆
    # 2. 用户信息保存在文件内
    # 3. 用户密码输入错误三次后锁定用户"
# i=0
# while i<3:
#     name=input('请输入用户名:').strip()
#     pwd=input('请输入密码:').strip()
#     if name=='aaaaaa' and pwd=='111111':
#         with open('data.txt',mode='w',encoding='utf8') as f:
#             f.write(name)
#             f.write(pwd)
#             break
#     else:
#         i+=1
#         print(i)
#         continue
# if i==3:
#     print('连续3次输入错误。')
#模拟登陆   END

