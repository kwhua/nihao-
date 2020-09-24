"""
1byte = 8bit
00000000 - 11111111  256
中国：每个汉字编一个号码
日本：每个日文编一个号码
ISO:UNICODE

"""
s = "请交作业"
print(len(s))  # 4

# str--->byte
# print(type(s))
# s2 = s.encode(encoding="utf8")  # b'\xe8\xaf\xb7\xe4\xba\xa4\xe4\xbd\x9c\xe4\xb8\x9a'
s2 = s.encode(encoding="gbk")

print(s2)
print(len(s2))
# print(type(s2))


#发送消息

# 接受消息
# 解码：bytes--->str
# s3 = s2.decode(encoding="utf8")
# print(s3)  # 正常显示
# s4 = s2.decode(encoding="gbk")
# print(s4)


