import hashlib
data='hello'
m=hashlib.md5(data.encode('utf8'))#MD5加密,加密对象格式是utf8
print(m.hexdigest())

m=hashlib.sha1(data.encode('utf8'))
print(m.hexdigest())

import zlib
import binascii
s = b'adfasdfasdfasdfgadfvfbsadfbsdfbsdfgsdfgsdfgfgsdfgsdfgvadcasdfadfaewa'
print(zlib.crc32(s))
# 1486392595
print(binascii.crc32(s))
# 1486392595


# string = "beyongjie"
# md5 = hashlib.md5()
# md5.update(string.encode('utf-8'))     #注意转码
# res = md5.hexdigest()
# print("md5加密结果:",res)