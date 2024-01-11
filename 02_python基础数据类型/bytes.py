"""
    1.字符集和编码
    0 1 <=> 1010101010 => 二进制的转换十进制 <=> 88
    电脑如何存储文字信息
    ...___ => a

    ascii => @#@@%@#@*&）*&）……  编排了128个文字符号 ，只需要7个0和1就可以表示 01111111 => 1byte => 8bit

    ANSI => 一套标准 每个字符 16bit , 2byte

    2.bytes
    用户平时看到的数据最终单位都是字节byte
"""
s = "周杰伦"
bs1 = s.encode("GBK") #b'\xd6\xdc\xbd\xdc\xc2\xd7'   bytes类型
bs2 = s.encode("UTF8") # b'\xe5\x91\xa8\xe6\x9d\xb0\xe4\xbc\xa6'
print(bs1)
print(bs2)

#怎么把一个gbk的字节转换成utf8的字节
bs = b'\xd6\xdc\xbd\xdc\xc2\xd7'
decode = bs.decode("gbk")
print(decode)
encode = decode.encode("UTF8")
print(encode)
