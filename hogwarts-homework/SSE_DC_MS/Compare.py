# coding: utf-8
import socket

import click
import numpy as np
import dpkt
import time
from CommUnpack import *

pcap_file = '/home/mingshuos/in.pcap'
client_pcap = '/home/mingshuos/out.pcap'
venue_addr = '10.208.32.22' #exchange src ip
# venue_addr = '168.168.89.62' #0328 #exchange src ip
client_addr = '233.0.0.1'
pcap_type = 1
mode = 1 #mode =1 :new udp // mode=2:old udp//
CIRCLE = 5 #FPGA circle
start_time=time.time()
list_venue = []
dict_client_3202 = {}
dict_client_3113 = {}
dict_client_3201 = {}
dict_client_9002 = {}
dict_client_5801 = {}
dict_client_1502 = {}
dict_client_5803 = {}
dict_client_3108 = {}
dict_client_3209 = {}
dict_client_3802 = {}
dict_client_3901 = {}

dict_venue_3202 = {}
dict_venue_3201 = {}
dict_venue_3113 = {}
dict_venue_9002 = {}
dict_venue_5801 = {}
dict_venue_3108 = {}
dict_venue_3209 = {}
dict_venue_3802 = {}
dict_venue_3901 = {}
dict_venue_5803 = {}
dict_venue_1502 = {}



FMT_TYPE = {
    'uInt8': 'B',
    'Int8': 'b',
    'uInt16': 'H',
    'Int16': 'h',
    'uInt32': 'I',
    'Int32': 'i',
    'string': 's',
    'char': 'c'
}
class EthData(object):

    def __init__(self):
        self.src_ip = ''
        self.src_port = 0
        self.dst_ip = ''
        self.dst_port = 0
        self.payload = ''
        self.ts_time = ''

    def __repr__(self):
        return "src_ip=" + self.src_ip + ' src_port=' + str(self.src_port) + ' dst_ip=' + self.dst_ip + ' dst_port=' + str(self.dst_port) + ' ts_time=' + str(self.ts_time) + ' payload=' + self.payload


class type_others:
    def __init__(self):
        self.type = ''
        self.securityid = ''
        self.msgseqid = ''
        self.capture_time = ''


class type_trade:
    def __init__(self):
        self.type = ''
        self.securityid = ''
        self.msgseqid = ''
        self.tradeindex = ''
        self.capture_time = ''


def get_value(fmt, str_hex):
    # print str_hex
    return struct.unpack(fmt, binascii.unhexlify(str_hex))[0]


def hex2Oct(hex_value, index=0):
    oct_value = int(hex_value.upper(), 16)
    return oct_value


def get_capture_time(str_hex):
    if str_hex.__len__() != 16:
         print(str_hex)
    #    assert False, 'str_hex len incorrect!'
    second_str = str_hex[0:8]
    nano_second_str = str_hex[8:16]
    second = int(str(second_str).upper(), 16)
    nano_second = int(str(nano_second_str).upper(), 16)
    return long(second * 10 ** 9 + nano_second)

def get_header_ts(pcap):
    f = open(pcap, 'r')
    pcap_ts = dpkt.pcap.Reader(f)
    return pcap_ts


def get_pcapstr(pcap):
    pkt = ''
    with open(pcap, 'rb') as f1:
        lines = f1.readlines()

    for index, line in enumerate(lines):
        pkt += binascii.hexlify(line)

    return pkt


class Cal_Len:
    def cal(self):
        list_type = ['UA3202', 'UA3201', 'UA3113', 'UA9002', 'UA5801','UA3108','UA3209','UA3802','UA3901','UA5803','UA1502']
        cu = CommUnpack()
        # pcap_str = get_pcapstr(pcap_file)
        # pcap_obj = Pcap()
        # pcap_iter = pcap_obj.get_pcap_obj(pcap_str)
        pcap_ts = get_header_ts(pcap_file)

        for (ts,buf) in pcap_ts:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            eth_data = EthData()


            if hasattr(ip, 'tcp'):
                tcp_src = socket.inet_ntoa(struct.pack('I', socket.htonl(int(binascii.b2a_hex(eth.data.src), 16))))
                if venue_addr in tcp_src:
                    eth_data.payload = binascii.b2a_hex(buf).decode()
                    if int(eth_data.payload[16 * 2: 16 * 2 + 2 * 2], 16) in (40, 44, 48):  # 40=空包，44/48=syn包，该处有风险，如果是业务报文也会丢弃
                        continue
                    eth_data.payload = eth_data.payload[54 * 2:]
                    payload = str(eth_data.payload)

        # for pkt in pcap_iter:
        #     try:
        #         # if 'IP' in pkt and venue_addr in pkt['IP'].src:
        #         if venue_addr in pcap_obj.pkt_body.ip.src_ip:
        #             payload = pcap_obj.pkt_body.data.str
        #             # payload = binascii.hexlify(str(pkt['TCP'].payload))
        #             if not payload.endswith('c3'):
        #                 print (payload)
        #                 print ('playload not end with c3!')
        #                 continue

                    fix_begin = payload.find('0133353d')
                    if fix_begin == -1:
                        continue
                    fix_begin += 8
                    type_end = payload[fix_begin:].find('01')
                    type_end += fix_begin
                    if type_end == -1:
                        continue
                    if type_end - fix_begin < 12:
                        continue
                    msg_type = get_value(str((type_end - fix_begin) / 2) + 's', payload[fix_begin:type_end])

                    if msg_type not in list_type:
                        continue

                    msgseqidpos = payload.find('31303037323d')
                    if msgseqidpos == -1:
                        continue
                    msgseqidpos += 12
                    posend = payload[msgseqidpos:].find('01') + msgseqidpos
                    lenth = (posend - msgseqidpos) / 2
                    msgseqid = get_value(str(lenth) + 's', payload[msgseqidpos:posend])
                    if pcap_type == 0:# test card
                        capture_time = get_capture_time(payload[-18:][:16])
                        # print(capture_time)
                    elif pcap_type == 1:#x10
                        capture_time = long(str(ts).replace('.',''))
                    elif pcap_type == 2: #mac ts
                        capture_time = get_value('q', payload[-16:])*CIRCLE


                    to = type_others()
                    if msg_type == 'UA9002':
                        security_id_list = re.findall('3.3.3.3.3.3.3.b.', payload[posend:])
                        for security_id in security_id_list:
                            slen = (len(security_id) - 2) / 2
                            to.securityid = get_value(str(slen) + 's', security_id[:-2]) + security_id[-1]
                            dict_key = str([to.securityid, msgseqid])
                            dict_venue_9002[dict_key] = capture_time
                    else:
                        security_id_list = re.findall('3.3.3.3.3.b.', payload[208:])
                        for security_id in security_id_list:
                            slen = (len(security_id) - 2) / 2
                            to.securityid = get_value(str(slen) + 's', security_id[:-2]) + security_id[-1]
                            dict_key = str([to.securityid, msgseqid])
                            if msg_type == 'UA3202':
                                dict_venue_3202[dict_key] = capture_time
                            elif msg_type == 'UA3201':
                                dict_venue_3201[dict_key] = capture_time
                            elif msg_type == 'UA3113':
                                dict_venue_3113[dict_key] = capture_time
                            elif msg_type == 'UA5801':
                                dict_venue_5801[dict_key] = capture_time
                            elif msg_type == 'UA3108':
                                dict_venue_3108[dict_key] = capture_time
                            elif msg_type == 'UA3209':
                                dict_venue_3209[dict_key] = capture_time
                            elif msg_type == 'UA3802':
                                dict_venue_3802[dict_key] = capture_time
                            elif msg_type == 'UA3901':
                                dict_venue_3901[dict_key] = capture_time
                            elif msg_type == 'UA5803':
                                dict_venue_5803[dict_key] = capture_time
                            elif msg_type == 'UA1502':
                                dict_venue_1502[dict_key] = capture_time
            # except Exception as e:
            #     print (e)
            #     print (binascii.hexlify(str(pkt)))
            #     continue
        # cl = PcapReader(client_pcap)

        # pcap_str = get_pcapstr(client_pcap)
        # pcap_obj = Pcap()
        # pcap_iter = pcap_obj.get_pcap_obj(pcap_str)
        #
        # for pkt in pcap_iter:
        #     try:
        #         # if 'IP' in pkt and (
        #         #         client_addr in pkt['IP'].dst or '234.0.0.1' in pkt['IP'].dst):  # 'UDP' in str(pkt) and
        #         if client_addr in pcap_obj.pkt_body.ip.dst_ip or '234.0.0.1' in pcap_obj.pkt_body.ip.dst_ip:
        #             # payload = binascii.hexlify(str(pkt['UDP'].payload))
        #             payload = pcap_obj.pkt_body.data.str
        #             if not payload.endswith('c3'):
        #                 # print payload
        #                 print ('playload not end with c3!')
        #                 continue
        pcap_uts = get_header_ts(client_pcap)
        for (ts, buf) in pcap_uts:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            eth_data = EthData()

            if hasattr(ip, 'udp'):
                udp_dst = socket.inet_ntoa(
                    struct.pack('I', socket.htonl(int(binascii.b2a_hex(eth.data.dst), 16))))
                if client_addr in udp_dst:
                    eth_data.payload = binascii.hexlify(buf).decode()
                    if int(eth_data.payload[16 * 2: 16 * 2 + 2 * 2], 16) in (
                            40, 44, 48):  # 40=空包，44/48=syn包，该处有风险，如果是业务报文也会丢弃
                        continue
                    eth_data.payload = eth_data.payload[84:]
                    payload = eth_data.payload
                    # if (str(ts).replace('.','')) == '1678957053499452327':
                    #     print(payload)
                    # payload ='01005e000001643f5f0193bb0800450001b40424400040113ed30a0a0237ea000001aa8356ce01a06ea9010100000001363030383135000000ff00543131310000000054524144450000000000006d0c0200fe0b0000da210000b0deafe70100000000c618cc43020000d60b0000ea0b000000000000fe0b0000cc0b000000000000000000000000000000000000b30b0000f07e096900000000920c0000c09b87c001000000900300000017b61d0100000040fcc4145201000033060000c0efc5e300000000e032e68f11010000e00b0000404b4c0000000000d60b0000a0271f0f00000000cc0b00001039911100000000c20b000000d78b1000000000b80b000020b15c2200000000ae0b000020fff10700000000a40b0000e0c03501000000009a0b000040d9580100000000900b000040fcea0000000000860b0000c031a80100000000ea0b00008018770900000000f40b0000e05dcb0a00000000fe0b0000c01b101400000000080c00008040f30f00000000120c0000407f2b0b000000001c0c0000a08abe1100000000260c0000c07fdc0b00000000300c00000077471e000000003a0c000020a7db1b00000000440c0000c0db021100000000141926035e2444f2'
                    # payload = '01005e000001000f53989aa10800450001748339400040119c89c0a86f0cea000001a5a856d401601e8b0c75dc000001313731393034000000ff0054524144450000c5e88c05a08601000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000bf05030000014d0c293312d7c3'
                    # payload = payload[84:]


                    if pcap_type == 0:
                        rst = cu.unpack(payload[:-18], msgid = mode)
                        capture_time = get_capture_time(payload[-18:][:16])
                    elif pcap_type == 1:
                        rst = cu.unpack(payload[:-8],msgid = mode) #msgid =1 :new udp // msgid =2:old udp//
                        capture_time = long(str(ts).replace('.',''))
                    elif pcap_type == 2:
                        rst = cu.unpack(payload[:-16], msgid=mode)
                        capture_time = get_value('q', payload[-16:]) * CIRCLE
                    dict_key = ''
                    if rst == None:
                        continue

                    if type(rst) == list:
                        for md in rst:
                            md.securityid = md.securityid.encode()
                            if md.type == '04':
                                md.msgSeqId = str(md.msgSeqId).lstrip('0')
                                dict_key = str([md.securityid[:6], md.msgSeqId])
                                if not dict_client_3201.has_key(dict_key):
                                    dict_client_3201[dict_key] = capture_time
                            elif md.type == '05':
                                md.msgSeqId = str(md.msgSeqId).lstrip('0')
                                dict_key = str([md.securityid[:6], md.msgSeqId])
                                if not dict_client_5801.has_key(dict_key):
                                    dict_client_5801[dict_key] = capture_time
                            elif md.type == '10':
                                dict_key = str([md.securityid[:6], str(md.MsgSeqID)])
                                if not dict_client_1502.has_key(dict_key):
                                    dict_client_1502[dict_key] = capture_time
                            elif md.type == '11':
                                dict_key = str([md.securityid[:6], str(md.MsgSeqID)])
                                if not dict_client_5803.has_key(dict_key):
                                    dict_client_5803[dict_key] = capture_time
                            if md.type == '07':
                                md.msgSeqId = str(md.msgSeqID).lstrip('0')
                                dict_key = str([md.securityid[:6], md.msgSeqId])
                                if not dict_client_3108.has_key(dict_key):
                                    dict_client_3108[dict_key] = capture_time
                            if md.type == '08':
                                md.msgSeqId = str(md.msgSeqID).lstrip('0')
                                dict_key = str([md.securityid[:6], md.msgSeqId])
                                if not dict_client_3209.has_key(dict_key):
                                    dict_client_3209[dict_key] = capture_time

                    else:
                        #rst.securityid = str(rst.securityid).encode()
                        msgtype = str(rst.type)
                        # if not msgtype in list_type:
                        #     continue
                        if msgtype == '01':
                            rst.msgSeqId = str(rst.msgSeqId).lstrip('0')
                            dict_key = str([rst.securityid[:6], rst.msgSeqId])
                            if not dict_client_3202.has_key(dict_key):
                                dict_client_3202[dict_key] = capture_time
                        elif msgtype == '02':
                            rst.msgSeqId = str(rst.msgSeqId).lstrip('0')
                            dict_key = str([rst.securityid[:6], rst.msgSeqId])
                            if not dict_client_3202.has_key(dict_key):
                                dict_client_3202[dict_key] = capture_time
                        elif msgtype == '03':
                            rst.msgSeqId = str(rst.msgSeqId).lstrip('0')
                            dict_key = str([rst.securityid[:6], rst.msgSeqId])
                            if not dict_client_3113.has_key(dict_key):
                                dict_client_3113[dict_key] = capture_time
                        elif msgtype == '0e':
                            dict_key = str([rst.securityid, str(rst.msgseqid).lstrip('0')])
                            if not dict_client_9002.has_key(dict_key):
                                dict_client_9002[dict_key] = capture_time
                        if msgtype == '0c':
                            rst.msgSeqId = str(rst.msgseqid).lstrip('0')
                            dict_key = str([rst.securityid[:6], rst.msgSeqId])
                            if not dict_client_3802.has_key(dict_key):
                                dict_client_3802[dict_key] = capture_time
                        if msgtype == '0d':
                            rst.msgseqid = str(rst.msgseqid).lstrip('0')
                            dict_key = str([rst.securityid[:6], rst.msgseqid])
                            if not dict_client_3901.has_key(dict_key):
                                dict_client_3901[dict_key] = capture_time


                else:
                    continue
            #
            # except Exception as e:
            #     print (e)
            #     print (binascii.hexlify(str(pkt)))
            #     continue


def get_mean(list_num):
    '''求中位数'''
    if list_num.__len__() % 2 != 0:
        return list_num[list_num.__len__() / 2]
    else:
        return (list_num[list_num.__len__() / 2] + list_num[list_num.__len__() / 2 - 1]) / 2.0



@click.command()
@click.option('--no', 'no', flag_value=True, default=False)
@click.option('--topic', required=True, nargs=1)
@click.option('--priv', required=True, nargs=1)
@click.argument('args', nargs=-1)
if __name__ == '__main__':
    list_latency = []
    Cal_Len().cal()
    f = open('rst.txt', 'w')
    f.truncate()
    f.close()
    f = open('rst.txt', 'a')

    print ('-------------------Snap-----------------------------')
    f.write('-------------------Snap-----------------------------\n')
    for dict_key in dict_venue_3202.keys():
        if dict_key in dict_client_3202:
            client_time = dict_client_3202[dict_key]
            latency = client_time - dict_venue_3202[dict_key]
            if latency < 0:
                continue
            list_latency.append(latency)
            f.write(str(dict_key) + ': venue_time=' + str(dict_venue_3202[dict_key]) + '  client_time=' + str(
                client_time) + '  latency=' + str(latency) + '\n')
            # print 'venue_time=', dict_venue_3202[dict_key], '  client_time=', client_time, '  latency=', latency
    if len(list_latency) > 0:
        list_latency.sort()
        print (len(list_latency))
        print ('venue total: ' + str(dict_venue_3202.keys().__len__()))
        print ('client total: ' + str(dict_client_3202.keys().__len__()))
        f.write('client total: ' + str(dict_client_3202.keys().__len__()) + '\n')
        f.write('min: ' + str(list_latency[0]) + '\n')
        f.write('median: ' + str(get_mean(list_latency)) + '\n')
        f.write('80fenwei: ' + str(np.percentile(list_latency, 80)))
        f.write('90fenwei: ' + str(np.percentile(list_latency, 90)))
        f.write('max: ' + str(list_latency[-1]) + '\n')
        f.write('average: ' + str(sum(list_latency) / list_latency.__len__()) + '\n')
        f.write('fangcha: %f' % np.var(list_latency) + '\n')
        f.write('biaozhuncha: %f' % np.std(list_latency) + '\n')

        print ('min: ', list_latency[0])
        print ('median: ', get_mean(list_latency))
        print ('80fenwei: ' + str(np.percentile(list_latency, 80)))
        print ('90fenwei: ' + str(np.percentile(list_latency, 90)))
        print ('99fenwei: ' + str(np.percentile(list_latency, 99)))
        print ('max: ', list_latency[-1])
        print ('average: ', sum(list_latency) / list_latency.__len__())
        print ('fangcha: %f' % np.var(list_latency))
        print ('biaozhuncha: %f' % np.std(list_latency) + '\n')

    print ('------------------Trade-----------------------------')
    f.write('-------------------Trade-----------------------------\n')
    list_latency = []
    for dict_key in dict_venue_3201.keys():
        if dict_key in dict_client_3201:
            client_time = dict_client_3201[dict_key]
            latency = client_time - dict_venue_3201[dict_key]
            if latency < 0:
                continue
            list_latency.append(latency)
            f.write(str(dict_key) + ': venue_time=' + str(dict_venue_3201[dict_key]) + '  client_time=' + str(
                client_time) + '  latency=' + str(latency) + '\n')
            # print 'venue_time=', dict_venue_3201[dict_key], '  client_time=', client_time, '  latency=', latency
    print ('venue total: ' + str(dict_venue_3201.keys().__len__()))
    print ('client total: ' + str(dict_client_3201.keys().__len__()))
    list_latency.sort()
    if len(list_latency) > 0:
        print (len(list_latency))
        f.write('client total: ' + str(dict_client_3201.keys().__len__()) + '\n')
        f.write('min: ' + str(list_latency[0]) + '\n')
        f.write('median: ' + str(get_mean(list_latency)) + '\n')
        f.write('80fenwei: ' + str(np.percentile(list_latency, 80)))
        f.write('90fenwei: ' + str(np.percentile(list_latency, 90)))
        f.write('max: ' + str(list_latency[-1]) + '\n')
        f.write('average: ' + str(sum(list_latency) / list_latency.__len__()) + '\n')
        f.write('fangcha: %f' % np.var(list_latency) + '\n')
        f.write('biaozhuncha: %f' % np.std(list_latency) + '\n')
        print ('min: ', list_latency[0])
        print ('median: ', get_mean(list_latency))
        print ('80fenwei: ' + str(np.percentile(list_latency, 80)))
        print ('90fenwei: ' + str(np.percentile(list_latency, 90)))
        print ('99fenwei: ' + str(np.percentile(list_latency, 99)))
        print ('max: ', list_latency[-1])
        print ('average: ', sum(list_latency) / list_latency.__len__())
        print ('fangcha: %f' % np.var(list_latency))
        print ('biaozhuncha: %f' % np.std(list_latency) + '\n')

    print ('------------------Order-----------------------------')
    f.write('-------------------Order-----------------------------\n')
    list_latency = []
    for dict_key in dict_venue_5801.keys():
        if dict_key in dict_client_5801:
            client_time = dict_client_5801[dict_key]
            latency = client_time - dict_venue_5801[dict_key]
            if latency < 0:
                continue
            list_latency.append(latency)
            f.write(str(dict_key) + ': venue_time=' + str(dict_venue_5801[dict_key]) + '  client_time=' + str(
                client_time) + '  latency=' + str(latency) + '\n')
            # print 'venue_time=', dict_venue_3201[dict_key], '  client_time=', client_time, '  latency=', latency
    print( 'venue total: ' + str(dict_venue_5801.keys().__len__()))
    print( 'client total: ' + str(dict_client_5801.keys().__len__()))
    list_latency.sort()
    if len(list_latency) > 0:
        print( len(list_latency))
        f.write('client total: ' + str(dict_client_5801.keys().__len__()) + '\n')
        f.write('min: ' + str(list_latency[0]) + '\n')
        f.write('median: ' + str(get_mean(list_latency)) + '\n')
        f.write('80fenwei: ' + str(np.percentile(list_latency, 80)))
        f.write('90fenwei: ' + str(np.percentile(list_latency, 90)))
        f.write('max: ' + str(list_latency[-1]) + '\n')
        f.write('average: ' + str(sum(list_latency) / list_latency.__len__()) + '\n')
        f.write('fangcha: %f' % np.var(list_latency) + '\n')
        f.write('biaozhuncha: %f' % np.std(list_latency) + '\n')
        print( 'min: ', list_latency[0])
        print( 'median: ', get_mean(list_latency))
        print ('80fenwei: ' + str(np.percentile(list_latency, 80)))
        print ('90fenwei: ' + str(np.percentile(list_latency, 90)))
        print ('99fenwei: ' + str(np.percentile(list_latency, 99)))
        print( 'max: ', list_latency[-1])
        print( 'average: ', sum(list_latency) / list_latency.__len__())
        print( 'fangcha: %f' % np.var(list_latency))
        print( 'biaozhuncha: %f' % np.std(list_latency) + '\n')

    print ('-------------------Idx-----------------------------')
    f.write('-------------------Idx-----------------------------\n')
    list_latency = []
    for dict_key in dict_venue_3113.keys():
        if dict_key in dict_client_3113:
            client_time = dict_client_3113[dict_key]
            latency = client_time - dict_venue_3113[dict_key]
            if latency < 0:
                continue
            list_latency.append(latency)
            f.write(str(dict_key) + ': venue_time=' + str(dict_venue_3113[dict_key]) + '  client_time=' + str(
                client_time) + '  latency=' + str(latency) + '\n')
            # print 'venue_time=', dict_venue_3113[dict_key], '  client_time=', client_time, '  latency=', latency
    if len(list_latency) > 0:
        list_latency.sort()
        print (len(list_latency))
        print ('venue total: ' + str(dict_venue_3113.keys().__len__()))
        print ('client total: ' + str(dict_client_3113.keys().__len__()))
        f.write('client total: ' + str(dict_client_3113.keys().__len__()) + '\n')
        f.write('min: ' + str(list_latency[0]) + '\n')
        f.write('median: ' + str(get_mean(list_latency)) + '\n')
        f.write('80fenwei: ' + str(np.percentile(list_latency, 80)))
        f.write('90fenwei: ' + str(np.percentile(list_latency, 90)))
        f.write('max: ' + str(list_latency[-1]) + '\n')
        f.write('average: ' + str(sum(list_latency) / list_latency.__len__()) + '\n')
        f.write('fangcha: %f' % np.var(list_latency) + '\n')
        f.write('biaozhuncha: %f' % np.std(list_latency) + '\n')
        print( 'min: ', list_latency[0])
        print( 'median: ', get_mean(list_latency))
        print ('80fenwei: ' + str(np.percentile(list_latency, 80)))
        print ('90fenwei: ' + str(np.percentile(list_latency, 90)))
        print ('99fenwei: ' + str(np.percentile(list_latency, 99)))
        print( 'max: ', list_latency[-1])
        print( 'average: ', sum(list_latency) / list_latency.__len__())
        print( 'fangcha: %f' % np.var(list_latency))
        print( 'biaozhuncha: %f' % np.std(list_latency) + '\n')

    print ('-------------------level1_option-----------------------------')
    f.write('-------------------level1_option-----------------------------\n')
    list_latency = []
    for dict_key in dict_venue_9002.keys():
        if dict_key in dict_client_9002:
            client_time = dict_client_9002[dict_key]
            latency = client_time - dict_venue_9002[dict_key]
            if latency < 0:
                continue
            list_latency.append(latency)
            f.write(str(dict_key) + ': venue_time=' + str(dict_venue_3113[dict_key]) + '  client_time=' + str(
                client_time) + '  latency=' + str(latency) + '\n')
    print( 'venue total: ' + str(dict_venue_9002.keys().__len__()))
    print( 'client total: ' + str(dict_client_9002.keys().__len__()))
    if len(list_latency) > 0:
        list_latency.sort()
        print (len(list_latency))
        f.write('client total: ' + str(dict_client_9002.keys().__len__()) + '\n')
        f.write('min: ' + str(list_latency[0]) + '\n')
        f.write('median: ' + str(get_mean(list_latency)) + '\n')
        f.write('80fenwei: ' + str(np.percentile(list_latency, 80)))
        f.write('90fenwei: ' + str(np.percentile(list_latency, 90)))
        f.write('max: ' + str(list_latency[-1]) + '\n')
        f.write('average: ' + str(sum(list_latency) / list_latency.__len__()) + '\n')
        f.write('fangcha: %f' % np.var(list_latency) + '\n')
        f.write('biaozhuncha: %f' % np.std(list_latency) + '\n')
        print ('min: ', list_latency[0])
        print ('median: ', get_mean(list_latency))
        print ('80fenwei: ' + str(np.percentile(list_latency, 80)))
        print ('90fenwei: ' + str(np.percentile(list_latency, 90)))
        print ('99fenwei: ' + str(np.percentile(list_latency, 99)))
        print ('max: ', list_latency[-1])
        print ('average: ', sum(list_latency) / list_latency.__len__())
        print ('fangcha: %f' % np.var(list_latency))
        print ('biaozhuncha: %f' % np.std(list_latency) + '\n')

    print ('-------------------Tick_Total_5803-----------------------------')
    f.write('-------------------Tick_Total_5803-----------------------------\n')
    list_latency = []
    for dict_key in dict_venue_5803.keys():
        if dict_key in dict_client_5803:
            client_time = dict_client_5803[dict_key]
            latency = client_time - dict_venue_5803[dict_key]
            if latency < 0:
                continue
            list_latency.append(latency)
            f.write(str(dict_key) + ': venue_time=' + str(dict_venue_5803[dict_key]) + '  client_time=' + str(
                client_time) + '  latency=' + str(latency) + '\n')

    if len(list_latency) > 0:
        list_latency.sort()
        print (len(list_latency))
        print ('venue total: ' + str(dict_venue_5803.keys().__len__()))
        print ('client total: ' + str(dict_client_5803.keys().__len__()))
        f.write('client total: ' + str(dict_client_5803.keys().__len__()) + '\n')
        f.write('min: ' + str(list_latency[0]) + '\n')
        f.write('median: ' + str(get_mean(list_latency)) + '\n')
        f.write('80fenwei: ' + str(np.percentile(list_latency, 80)))
        f.write('90fenwei: ' + str(np.percentile(list_latency, 90)))
        f.write('max: ' + str(list_latency[-1]) + '\n')
        f.write('average: ' + str(sum(list_latency) / list_latency.__len__()) + '\n')
        f.write('fangcha: %f' % np.var(list_latency) + '\n')
        f.write('biaozhuncha: %f' % np.std(list_latency) + '\n')

        print ('min: ', list_latency[0])
        print ('median: ', get_mean(list_latency))
        print ('80fenwei: ' + str(np.percentile(list_latency, 80)))
        print ('90fenwei: ' + str(np.percentile(list_latency, 90)))
        print ('99fenwei: ' + str(np.percentile(list_latency, 99)))
        print ('max: ', list_latency[-1])
        print ('average: ', sum(list_latency) / list_latency.__len__())
        print ('fangcha: %f' % np.var(list_latency))
        print ('biaozhuncha: %f' % np.std(list_latency) + '\n')

    print ('-------------------ETF_1502-----------------------------')
    f.write('-------------------ETF_1502-----------------------------\n')
    list_latency = []
    for dict_key in dict_venue_1502.keys():
        if dict_key in dict_client_1502:
            client_time = dict_client_1502[dict_key]
            latency = client_time - dict_venue_1502[dict_key]
            if latency < 0:
                continue
            list_latency.append(latency)
            f.write(str(dict_key) + ': venue_time=' + str(dict_venue_1502[dict_key]) + '  client_time=' + str(
                client_time) + '  latency=' + str(latency) + '\n')

    if len(list_latency) > 0:
        list_latency.sort()
        print (len(list_latency))
        print ('venue total: ' + str(dict_venue_1502.keys().__len__()))
        print ('client total: ' + str(dict_client_1502.keys().__len__()))
        f.write('client total: ' + str(dict_client_1502.keys().__len__()) + '\n')
        f.write('min: ' + str(list_latency[0]) + '\n')
        f.write('median: ' + str(get_mean(list_latency)) + '\n')
        f.write('80fenwei: ' + str(np.percentile(list_latency, 80)))
        f.write('90fenwei: ' + str(np.percentile(list_latency, 90)))
        f.write('max: ' + str(list_latency[-1]) + '\n')
        f.write('average: ' + str(sum(list_latency) / list_latency.__len__()) + '\n')
        f.write('fangcha: %f' % np.var(list_latency) + '\n')
        f.write('biaozhuncha: %f' % np.std(list_latency) + '\n')

        print ('min: ', list_latency[0])
        print ('median: ', get_mean(list_latency))
        print ('80fenwei: ' + str(np.percentile(list_latency, 80)))
        print ('90fenwei: ' + str(np.percentile(list_latency, 90)))
        print ('99fenwei: ' + str(np.percentile(list_latency, 99)))
        print ('max: ', list_latency[-1])
        print ('average: ', sum(list_latency) / list_latency.__len__())
        print ('fangcha: %f' % np.var(list_latency))
        print ('biaozhuncha: %f' % np.std(list_latency) + '\n')

    print ('-------------------TradeEndOfDay3108-----------------------------')
    f.write('-------------------TradeEndOfDay3108-----------------------------\n')
    list_latency = []
    for dict_key in dict_venue_3108.keys():
        if dict_key in dict_client_3108:
            client_time = dict_client_3108[dict_key]
            latency = client_time - dict_venue_3108[dict_key]
            if latency < 0:
                continue
            list_latency.append(latency)
            f.write(str(dict_key) + ': venue_time=' + str(dict_venue_3108[dict_key]) + '  client_time=' + str(
                client_time) + '  latency=' + str(latency) + '\n')

    if len(list_latency) > 0:
        list_latency.sort()
        print (len(list_latency))
        print ('venue total: ' + str(dict_venue_3108.keys().__len__()))
        print ('client total: ' + str(dict_client_3108.keys().__len__()))
        f.write('client total: ' + str(dict_client_3108.keys().__len__()) + '\n')
        f.write('min: ' + str(list_latency[0]) + '\n')
        f.write('median: ' + str(get_mean(list_latency)) + '\n')
        f.write('80fenwei: ' + str(np.percentile(list_latency, 80)))
        f.write('90fenwei: ' + str(np.percentile(list_latency, 90)))
        f.write('max: ' + str(list_latency[-1]) + '\n')
        f.write('average: ' + str(sum(list_latency) / list_latency.__len__()) + '\n')
        f.write('fangcha: %f' % np.var(list_latency) + '\n')
        f.write('biaozhuncha: %f' % np.std(list_latency) + '\n')

        print ('min: ', list_latency[0])
        print ('median: ', get_mean(list_latency))
        print ('80fenwei: ' + str(np.percentile(list_latency, 80)))
        print ('90fenwei: ' + str(np.percentile(list_latency, 90)))
        print ('99fenwei: ' + str(np.percentile(list_latency, 99)))
        print ('max: ', list_latency[-1])
        print ('average: ', sum(list_latency) / list_latency.__len__())
        print ('fangcha: %f' % np.var(list_latency))
        print ('biaozhuncha: %f' % np.std(list_latency) + '\n')

    print ('-------------------MktData3209-----------------------------')
    f.write('-------------------MktData3209-----------------------------\n')
    list_latency = []
    for dict_key in dict_venue_3209.keys():
        if dict_key in dict_client_3209:
            client_time = dict_client_3209[dict_key]
            latency = client_time - dict_venue_3209[dict_key]
            if latency < 0:
                continue
            list_latency.append(latency)
            f.write(str(dict_key) + ': venue_time=' + str(dict_venue_3209[dict_key]) + '  client_time=' + str(
                client_time) + '  latency=' + str(latency) + '\n')

    if len(list_latency) > 0:
        list_latency.sort()
        print (len(list_latency))
        print ('venue total: ' + str(dict_venue_3209.keys().__len__()))
        print ('client total: ' + str(dict_client_3209.keys().__len__()))
        f.write('client total: ' + str(dict_client_3209.keys().__len__()) + '\n')
        f.write('min: ' + str(list_latency[0]) + '\n')
        f.write('median: ' + str(get_mean(list_latency)) + '\n')
        f.write('80fenwei: ' + str(np.percentile(list_latency, 80)))
        f.write('90fenwei: ' + str(np.percentile(list_latency, 90)))
        f.write('max: ' + str(list_latency[-1]) + '\n')
        f.write('average: ' + str(sum(list_latency) / list_latency.__len__()) + '\n')
        f.write('fangcha: %f' % np.var(list_latency) + '\n')
        f.write('biaozhuncha: %f' % np.std(list_latency) + '\n')

        print ('min: ', list_latency[0])
        print ('median: ', get_mean(list_latency))
        print ('80fenwei: ' + str(np.percentile(list_latency, 80)))
        print ('90fenwei: ' + str(np.percentile(list_latency, 90)))
        print ('99fenwei: ' + str(np.percentile(list_latency, 99)))
        print ('max: ', list_latency[-1])
        print ('average: ', sum(list_latency) / list_latency.__len__())
        print ('fangcha: %f' % np.var(list_latency))
        print ('biaozhuncha: %f' % np.std(list_latency) + '\n')

    print ('-------------------bond_snap_3802-----------------------------')
    f.write('-------------------bond_snap_3802-----------------------------\n')
    list_latency = []
    for dict_key in dict_venue_3802.keys():
        if dict_key in dict_client_3802:
            client_time = dict_client_3802[dict_key]
            latency = client_time - dict_venue_3802[dict_key]
            if latency < 0:
                continue
            list_latency.append(latency)
            f.write(str(dict_key) + ': venue_time=' + str(dict_venue_3802[dict_key]) + '  client_time=' + str(
                client_time) + '  latency=' + str(latency) + '\n')

    if len(list_latency) > 0:
        list_latency.sort()
        print (len(list_latency))
        print ('venue total: ' + str(dict_venue_3802.keys().__len__()))
        print ('client total: ' + str(dict_client_3802.keys().__len__()))
        f.write('client total: ' + str(dict_client_3802.keys().__len__()) + '\n')
        f.write('min: ' + str(list_latency[0]) + '\n')
        f.write('median: ' + str(get_mean(list_latency)) + '\n')
        f.write('80fenwei: ' + str(np.percentile(list_latency, 80)))
        f.write('90fenwei: ' + str(np.percentile(list_latency, 90)))
        f.write('max: ' + str(list_latency[-1]) + '\n')
        f.write('average: ' + str(sum(list_latency) / list_latency.__len__()) + '\n')
        f.write('fangcha: %f' % np.var(list_latency) + '\n')
        f.write('biaozhuncha: %f' % np.std(list_latency) + '\n')

        print ('min: ', list_latency[0])
        print ('median: ', get_mean(list_latency))
        print ('80fenwei: ' + str(np.percentile(list_latency, 80)))
        print ('90fenwei: ' + str(np.percentile(list_latency, 90)))
        print ('99fenwei: ' + str(np.percentile(list_latency, 99)))
        print ('max: ', list_latency[-1])
        print ('average: ', sum(list_latency) / list_latency.__len__())
        print ('fangcha: %f' % np.var(list_latency))
        print ('biaozhuncha: %f' % np.std(list_latency) + '\n')

    print ('-------------------bond_tick_by_tick_3901-----------------------------')
    f.write('-------------------bond_tick_by_tick_3901-----------------------------\n')
    list_latency = []
    for dict_key in dict_venue_3901.keys():
        if dict_key in dict_client_3901:
            client_time = dict_client_3901[dict_key]
            latency = client_time - dict_venue_3901[dict_key]
            if latency < 0:
                continue
            list_latency.append(latency)
            f.write(str(dict_key) + ': venue_time=' + str(dict_venue_3901[dict_key]) + '  client_time=' + str(
                client_time) + '  latency=' + str(latency) + '\n')

    if len(list_latency) > 0:
        list_latency.sort()
        print (len(list_latency))
        print ('venue total: ' + str(dict_venue_3901.keys().__len__()))
        print ('client total: ' + str(dict_client_3901.keys().__len__()))
        f.write('client total: ' + str(dict_client_3901.keys().__len__()) + '\n')
        f.write('min: ' + str(list_latency[0]) + '\n')
        f.write('median: ' + str(get_mean(list_latency)) + '\n')
        f.write('80fenwei: ' + str(np.percentile(list_latency, 80)))
        f.write('90fenwei: ' + str(np.percentile(list_latency, 90)))
        f.write('max: ' + str(list_latency[-1]) + '\n')
        f.write('average: ' + str(sum(list_latency) / list_latency.__len__()) + '\n')
        f.write('fangcha: %f' % np.var(list_latency) + '\n')
        f.write('biaozhuncha: %f' % np.std(list_latency) + '\n')

        print ('min: ', list_latency[0])
        print ('median: ', get_mean(list_latency))
        print ('80fenwei: ' + str(np.percentile(list_latency, 80)))
        print ('90fenwei: ' + str(np.percentile(list_latency, 90)))
        print ('99fenwei: ' + str(np.percentile(list_latency, 99)))
        print ('max: ', list_latency[-1])
        print ('average: ', sum(list_latency) / list_latency.__len__())
        print ('fangcha: %f' % np.var(list_latency))
        print ('biaozhuncha: %f' % np.std(list_latency) + '\n')
print(time.time() - start_time)
