import struct
import binascii
import re

EXCHANGE_ID = '01'


def hex2Oct(hex_value):
    try:
        oct_value = int(hex_value.upper(), 16)
        return oct_value
    except Exception as e:
        print (hex_value)
        print (e)
        return


def get_value(fmt, str_hex):
    value = struct.unpack(fmt, binascii.unhexlify(str_hex))[0]
    if 's' in fmt:
        value = str(str(value))
    elif 'd' in fmt:
        value = round(value, 5)
    return value


def get_msgseqid(hex_str,mode=1):
    if len(hex_str) == 8 and mode ==1:
        ss = get_value('i', hex_str)
    elif len(hex_str) != 8 and mode ==1:
        d = re.findall(r'.{2}', hex_str)
        d.reverse()
        ss = str(''.join(d))
    elif mode==2:
        d = re.findall(r'.{2}', hex_str)
        d.reverse()
        ss = str(''.join(d))
    return ss



# if __name__ == '__main__':
#     hex_str = '313931'
#     a = get_value('3s',hex_str)
#     print(a)
