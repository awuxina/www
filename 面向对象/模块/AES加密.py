# 安装插件 pip install pycryptodome
from Crypto.Cipher import AES
class MyAES:
    def __format16(self,text):
        length = len(text)
        text = bytearray(text, encoding='utf-8')
        remainder = length % 16
        if remainder == 0:
            num = 16
        else:
            num = 16 - remainder
        for i in range(num):
            text.append(length)
        return text

    def __init__(self,code):
        # 将密码转换为16位
        self.code = self.__format16(code)
        #设置密码与模式
        self.aes = AES.new(self.code, AES.MODE_ECB)


    def encode(self,text):
        return self.aes.encrypt(self.__format16(text))

    def decode(self,text):
        text = str(self.aes.decrypt(text),encoding='utf-8',errors="ignore")
        num =ord(text[-1])
        return text[0:num]
