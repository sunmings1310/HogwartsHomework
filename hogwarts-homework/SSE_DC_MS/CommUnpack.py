from __future__ import division
from CommonStruct import *
import os
from __init__ import *


class CommUnpack:
    def __init__(self):
        self.sequence = 0
        self.szse_value = 1000000
        self.szse_qty = 100
        self.szse_amt = 10000
        self.sse_others = 1000
        self.sse_amt = 100000
        self.sse_10 = 10

    def unpack(self, data, iswrite=0, old=False, msgid=1):
        data = data.strip()
        type = data[:2]
        sequence = hex2Oct(data[2:10])
        exchange_id = data[10:12]
        self.sequence = sequence
        if exchange_id != '01':
            print(data)
        if exchange_id == '01':  # sse_md
            try:
                if type == '01':  # composite info md
                    cc = Snap()
                    cc.sequence = sequence
                    cc.exchange_id = exchange_id
                    cc.securityid = get_value('9s', data[12:30])
                    cc.flag = get_msgseqid(data[30:34])  # transfer little endian to big-endian
                    cc.tradingphasecode = get_value('8s', data[34:50])
                    cc.instrumentStatus = get_value('6s', data[50:62])
                    cc.timestamp = get_value('i', data[72:80])
                    cc.preclose_price = get_value('i', data[80:88])
                    cc.numtrades = get_value('i', data[88:96])
                    cc.totalvolumetrade = get_value('q', data[96:112])
                    cc.totalvaluetrade = get_value('q', data[112:128])
                    cc.last_price = get_value('i', data[128:136])
                    cc.open_price = get_value('i', data[136:144])
                    cc.close_price = get_value('i', data[144:152])
                    cc.high_price = get_value('i', data[152:160])
                    cc.low_price = get_value('i', data[160:168])
                    cc.bid_avg_price = get_value('i', data[200:208])
                    cc.bid_total_qty = get_value('q', data[208:224])
                    cc.ask_avg_price = get_value('i', data[224:232])
                    cc.ask_total_qty = get_value('q', data[232:248])
                    i = 248
                    if len(data) == 408 * 2 and msgid == 2:
                        cc.withDrawBuyNumber = get_value('i', data[248:256])
                        cc.withDrawBuyAmount = get_value('q', data[256:272])
                        cc.withDrawBuyAmount = get_value('q', data[272:288])
                        cc.withDrawSellNumber = get_value('i', data[288:296])
                        cc.withDrawSellAmount = get_value('q', data[296:312])
                        cc.withDrawSellAmount = get_value('q', data[312:328])
                        i = 328

                    for j in range(10):
                        cc.bid_price_list.append(get_value('i', data[i:i + 8]))
                        cc.bid_vol_list.append(get_value('q', data[i + 8:i + 24]))
                        i += 24
                    for k in range(10):
                        cc.ask_price_list.append(get_value('i', data[i:i + 8]))
                        cc.ask_vol_list.append(get_value('q', data[i + 8:i + 24]))
                        i += 24

                    if msgid == 1:
                        cc.msgSeqId = get_msgseqid(data[i:i + 8])
                    elif msgid == 2:
                        cc.msgSeqId = get_msgseqid(data[i:i + 8], 2)

                    if iswrite == 1:
                        self.write_new_file(cc.timestamp, data)
                    return cc

                elif type == '02':  # 50 orders md
                    odr = Orders()
                    odr.sequence = sequence
                    odr.exchange_id = exchange_id
                    odr.securityid = get_value('9s', data[12:30])
                    odr.mdstreamid = data[36:44]
                    odr.side = get_value('b', data[44:46])
                    odr.order_numbers = get_value('b', data[46:48])
                    odr.timestamp = get_value('i', data[48:56])
                    odr.price = get_value('i', data[56:64])
                    odr.qty = get_value('q', data[64:80])
                    i = 80
                    for j in range(odr.order_numbers):
                        odr.volume_list.append(get_value('q', data[i:i + 16]))
                        i += 16

                    if iswrite == 1:
                        self.write_new_file(odr.timestamp, data)
                    return odr

                elif type == '03':  # index md
                    idx = IndexMd()
                    idx.sequence = sequence
                    idx.exchange_id = data[10:12]
                    idx.securityid = get_value('9s', data[12:30])
                    idx.flag = get_msgseqid(data[30:32])  # transfer little endian to big-endian
                    idx.timestamp = get_value('i', data[40:48])
                    idx.tradeTime = get_value('i', data[48:56])
                    if msgid == 1:
                        idx.msgSeqId = get_msgseqid(data[56:64])
                    elif msgid == 2:
                        idx.msgSeqId = get_msgseqid(data[56:64], 2)
                    idx.preclose_price = get_value('q', data[64:80])
                    idx.open_price = get_value('q', data[80:96])
                    idx.last_price = get_value('q', data[96:112])
                    idx.high_price = get_value('q', data[112:128])
                    idx.low_price = get_value('q', data[128:144])
                    idx.closeIndex = get_value('q', data[144:160])
                    idx.total_volume = get_value('q', data[160:176])
                    idx.total_value = get_value('q', data[176:192])

                    if iswrite == 1:
                        self.write_new_file(idx.timestamp, data)
                    return idx

                elif type == '04' and not old:  # trade by line md
                    i = 0
                    list_trade = []
                    while i < len(data):
                        trd_md = data[i:]  # struct for 64 Byte
                        trade = TradeByLine()
                        trade.sequence = sequence
                        trade.exchange_id = data[10:12]
                        trade.securityid = get_value('9s', trd_md[12:30])
                        trade.TradeBSFlag = get_value('1s', trd_md[30:32])
                        trade.applseqnum = get_value('i', trd_md[32:40])
                        trade.channelno = get_value('i', trd_md[40:48])
                        trade.transacttime = get_value('i', trd_md[48:56])
                        trade.tradePrice = get_value('i', trd_md[56:64])
                        trade.tradeQty = get_value('q', trd_md[64:80])
                        trade.trademoney = get_value('q', trd_md[80:96])
                        trade.tradeBuyNo = get_value('q', trd_md[96:112])
                        trade.tradeSellNo = get_value('q', trd_md[112:128])
                        trade.bizIndex = get_value('q', trd_md[128:144])
                        if msgid == 1:
                            trade.msgSeqId = get_msgseqid(trd_md[144:152])
                        elif msgid == 2:
                            trade.msgSeqId = get_msgseqid(trd_md[144:152], 2)

                        if iswrite == 1:
                            self.write_new_file(trade.transacttime, trd_md)
                        list_trade.append(trade)
                        i += 160
                    return list_trade

                elif type == '04' and old:
                    i = 0
                    list_trade = []
                    while i < len(data):
                        trd_md = data[i:]
                        trade = TradeByLineOld()
                        trade.sequence = sequence
                        trade.exchange_id = trd_md[10:12]
                        trade.securityid = get_value('8s', trd_md[12:28])
                        trade.exec_type = trd_md[28:30]
                        trade.TradeBSFlag = get_value('1s', trd_md[30:32])
                        trade.applseqnum = hex2Oct(trd_md[40:48])
                        trade.transacttime = get_value('q', (trd_md[48:64]))
                        trade.tradePrice = get_value('q', (trd_md[64:80]))
                        trade.tradeQty = get_value('q', (trd_md[80:96]))
                        trade.trademoney = get_value('q', (trd_md[96:112]))
                        trade.tradeBuyNo = get_value('q', (trd_md[112:128]))
                        trade.tradeSellNo = get_value('q', (trd_md[128:144]))
                        trade.channelno = get_value('i', (trd_md[144:152]))
                        trade.mdstreamid = trd_md[152:158]
                        if msgid == 1:
                            trade.msgSeqId = get_msgseqid(trd_md[158:166])
                        elif msgid == 2:
                            trade.msgSeqId = get_msgseqid(trd_md[158:166], 2)
                        trade.sendingTime = get_value('6s', trd_md[166:178])

                        if iswrite == 1:
                            self.write_new_file(trade.transacttime, trd_md)
                        list_trade.append(trade)
                        i += 192
                    return list_trade

                elif type == '05':  # 5801
                    i = 0
                    list_entrust = []
                    while i < len(data):
                        entrust_md = data[i:]
                        entrust = EntrustByLine()
                        entrust.sequence = sequence
                        entrust.exchange_id = entrust_md[10:12]
                        entrust.securityid = get_value('9s', entrust_md[12:30])
                        entrust.orderType = get_value('1s', entrust_md[30:32])
                        entrust.orderBSFlag = get_value('1s', entrust_md[32:34])
                        entrust.orderIndex = get_value('i', entrust_md[34:42])
                        entrust.channelno = get_value('i', entrust_md[42:50])
                        entrust.orderTime = get_value('i', entrust_md[50:58])
                        entrust.orderNo = get_value('q', entrust_md[58:74])
                        entrust.orderPrice = get_value('i', entrust_md[74:82])
                        entrust.balance = get_value('q', entrust_md[82:98])
                        entrust.bizIndex = get_value('q', entrust_md[98:114])
                        if msgid == 1:
                            entrust.msgSeqId = get_msgseqid(entrust_md[114:122])
                        elif msgid == 2:
                            entrust.msgSeqId = get_msgseqid(entrust_md[114:122], 2)
                        i += 128
                        list_entrust.append(entrust)
                    return list_entrust
                elif type == '11':  # 5803
                    i = 0
                    list_md = []
                    while i < len(data):
                        md = data[i:]
                        tt = Tick_Total_5803()
                        tt.sequence = sequence
                        tt.exchange_id = md[10:12]
                        tt.securityid = get_value('9s', md[12:30])
                        tt.TickType = get_value('1s', md[30:32])
                        tt.TickBSFlag = get_value('1s', md[32:34])
                        tt.Tickindex = get_value('q', md[34:50])
                        tt.Channel = get_value('i', md[50:58])
                        tt.TickTime = get_value('i', md[58:66])
                        tt.BuyOrderNo = get_value('q', md[66:82])
                        tt.SellOrderNo = get_value('q', md[82:98])
                        tt.Price = get_value('i', md[98:106])
                        tt.Qty = get_value('q', md[106:122])
                        tt.TradeMoney = get_value('q', md[122:138])
                        tt.MsgSeqID = get_value('i', md[138:146])
                        tt.Rsvd = md[146:160]
                        i += 160
                        list_md.append(tt)
                    return list_md
                elif type == '10':  # 1502
                    i = 0
                    list_md = []
                    while i < len(data):
                        md = data[i:]
                        etf = ETF_1502()
                        etf.sequence = sequence
                        etf.exchange_id = md[10:12]
                        etf.securityid = get_value('9s', md[12:30])
                        etf.TimeStamp = get_value('i', md[30:38])
                        etf.ETFBuyNumber = get_value('i', md[38:46])
                        etf.ETFBuyAmount = get_value('q', md[46:62])
                        etf.ETFBuyMoney = get_value('q', md[62:78])
                        etf.ETFSellNumber = get_value('i', md[78:86])
                        etf.ETFSellAmount = get_value('q', md[86:102])
                        etf.ETFSellMoney = get_value('q', md[102:118])
                        etf.MsgSeqID = get_value('i', md[118:126])
                        etf.Rsvd = md[126:128]
                        i += 128
                        list_md.append(etf)
                    return list_md

                elif type == '07':  # UA3108
                    ua3108 = TradeEndOfDay3108()
                    ua3108.sequence = data[2:10]
                    ua3108.exchange_id = data[10:12]
                    ua3108.securityid = get_value('9s', data[12:30])
                    ua3108.flag = get_msgseqid(data[30:32])  # transfer little-endian into big-endian
                    ua3108.instrumentStatus = get_value('6s', data[32:44])
                    ua3108.datatimeStamp = get_value('i', data[44:52])
                    ua3108.closePx = get_value('i', data[52:60])
                    ua3108.numTrades = get_value('i', data[60:68])
                    ua3108.totalVolumeTrade = get_value('q', data[68:84])
                    ua3108.totalValueTrade = get_value('q', data[84:100])
                    ua3108.totalBidQty = get_value('q', data[100:116])
                    ua3108.totalSellQty = get_value('q', data[116:132])
                    ua3108.withDrawBuyNumber = get_value('i', data[132:140])
                    ua3108.withDrawBuyAmount = get_value('q', data[140:156])
                    ua3108.withDrawSellNumber = get_value('i', data[156:164])
                    ua3108.withDrawSellAmount = get_value('q', data[164:180])
                    if msgid == 1:
                        ua3108.msgSeqID = get_msgseqid(data[180:188])
                    elif msgid == 2:
                        ua3108.msgSeqID = get_msgseqid(data[180:188], 2)
                    ua3108.noBidLevel = get_value('i', data[188:196])
                    ua3108.noOfferLevel = get_value('i', data[196:204])
                    idx = 204
                    if ua3108.noBidLevel != 0 and ua3108.noOfferLevel != 0:
                        ua3108.bidOrderQty = get_value('q', data[idx:idx + 16])
                        idx += 16
                        ua3108.askOrderQty = get_value('q', data[idx:idx + 16])
                        idx += 16
                        ua3108.bidNoOrders = get_value('q', data[idx:idx + 16])
                        idx += 16
                        ua3108.askNoOrders = get_value('q', data[idx:idx + 16])
                        idx += 16
                        # if ua3108.bidNoOrders > 0:
                        #     for i in range(ua3108.bidNoOrders):
                        #         ua3108.bidOrderQty50.append(get_value('q',data[idx:idx+16]))
                        #         idx += 16
                        # if ua3108.askNoOrders > 0:
                        #     for i in range(ua3108.askNoOrders):
                        #         ua3108.askOrderQty50.append(get_value('q',data[idx:idx+16]))
                        #         idx += 16
                    elif ua3108.noBidLevel != 0 and ua3108.noOfferLevel == 0:
                        ua3108.bidOrderQty = get_value('q', data[idx:idx + 16])
                        idx += 16
                        # ua3108.bidNoOrders = get_value('q',data[idx:idx + 16])
                        # idx += 16
                        # if ua3108.bidNoOrders > 0:
                        #     for i in range(ua3108.bidNoOrders):
                        #         ua3108.bidOrderQty50.append(get_value('q',data[idx:idx + 16]))
                        #         idx += 16
                    elif ua3108.noBidLevel == 0 and ua3108.noOfferLevel != 0:
                        ua3108.askOrderQty = get_value('q', data[idx:idx + 16])
                        idx += 16
                        # ua3108.askNoOrders = get_value('q',data[idx:idx+16])
                        # idx += 16
                        # if ua3108.askNoOrders > 0:
                        #     for i in range(ua3108.askNoOrders):
                        #         ua3108.askOrderQty50.append(get_value('q',data[idx:idx+16]))
                        #         idx += 16
                    return ua3108
                elif type == '08':
                    idx = 0
                    list_ua3209 = []
                    while idx < len(data):
                        ua3209 = MktData3209()
                        md = data[idx:idx + 144]
                        ua3209.sequence = md[2:10]
                        ua3209.exchange_id = md[10:12]
                        ua3209.securityid = get_value('9s', md[12:30])
                        ua3209.tradeBSFlag = get_value('1s', md[30:32])
                        ua3209.tradeindex = get_value('i', md[32:40])
                        ua3209.channelno = get_value('i', md[40:48])
                        ua3209.tradeTime = get_value('i', md[48:56])
                        ua3209.tradeprice = get_value('i', md[56:64])
                        ua3209.tradeqty = get_value('q', md[64:80])
                        ua3209.trademoney = get_value('q', md[80:96])
                        ua3209.tradebuyno = get_value('q', md[96:112])
                        ua3209.tradesellno = get_value('q', md[112:128])
                        if msgid == 1:
                            ua3209.msgSeqID = get_msgseqid(md[128:136])
                        elif msgid == 2:
                            ua3209.msgSeqID = get_msgseqid(md[128:136], 2)
                        idx += 144
                        list_ua3209.append(ua3209)
                    return list_ua3209


                elif type == '0e':  # option_level1
                    opt = OptionLv1()
                    opt.sequence = data[2:10]
                    opt.exchange_id = data[10:12]
                    opt.securityid = get_value('9s', data[12:30])
                    opt.tradeVolume = get_value('q', data[32:48])
                    opt.totalValueTraded = get_value('q', data[48:64])
                    opt.totalLongPosition = get_value('q', data[64:80])
                    opt.preClosePrice = get_value('q', data[80:96])
                    opt.prevSetPrice = get_value('q', data[96:112])
                    opt.tradePrice = get_value('q', data[112:128])
                    opt.openPrice = get_value('q', data[128:144])
                    opt.closePrice = get_value('q', data[144:160])
                    opt.settlePrice = get_value('q', data[160:176])
                    opt.highPrice = get_value('q', data[176:192])
                    opt.lowPrice = get_value('q', data[192:208])
                    opt.auctionPrice = get_value('q', data[208:224])
                    opt.auctionQty = get_value('q', data[224:240])
                    opt.tradingPhaseCode = get_value('8s', data[240:256])
                    idx = 256
                    for i in range(5):
                        opt.bidPrice.append(get_value('q', data[idx:idx + 16]))
                        idx += 16
                        opt.bidVolume.append(get_value('q', data[idx:idx + 16]))
                        idx += 16
                    for i in range(5):
                        opt.askPrice.append(get_value('q', data[idx:idx + 16]))
                        idx += 16
                        opt.askVolume.append(get_value('q', data[idx:idx + 16]))
                        idx += 16
                    if msgid == 1:
                        opt.msgseqid = get_msgseqid(data[idx:idx + 8])
                    elif msgid == 2:
                        opt.msgseqid = get_msgseqid(data[idx:idx + 8], 2)
                    idx += 8
                    opt.uptimeStamp_s = get_msgseqid(data[idx:idx + 8])  # transfer bid-endian into little-endian
                    idx += 8
                    opt.uptimeStamp_ms = get_msgseqid(data[idx:idx + 4])
                    return opt
                elif type == '0c' and msgid == 1:
                    bs = bond_snap()
                    bs.sequence = data[2:10]
                    bs.exchange_id = data[10:12]
                    bs.securityid = get_value('9s', data[12:30])
                    bs.flag = data[30:34]
                    bs.instrumentstatus = get_value('6s', data[34:46])
                    bs.rsvd = data[46:48]
                    bs.timestamp = get_value('i', data[48:56])
                    bs.preclose_price = get_value('i', data[56:64])
                    bs.open_price = get_value('i', data[64:72])
                    bs.high_price = get_value('i', data[72:80])
                    bs.low_price = get_value('i', data[80:88])
                    bs.last_price = get_value('i', data[88:96])
                    bs.close_price = get_value('i', data[96:104])
                    bs.num_trades = get_value('i', data[104:112])
                    bs.total_volume_trade = get_value('q', data[112:128])
                    bs.total_value_trade = get_value('q', data[128:144])
                    bs.total_bid_qty = get_value('q', data[144:160])
                    bs.avg_bid_price = get_value('i', data[160:168])
                    bs.total_offer_qty = get_value('q', data[168:184])
                    bs.avg_offer_price = get_value('i', data[184:192])
                    bs.avg_price = get_value('i', data[192:200])
                    i = 200
                    for t in range(10):
                        bs.bid_price.append(get_value('i', data[i: i + 8]))
                        bs.bid_volume.append(get_value('q', data[i + 8:i + 24]))
                        i += 24
                    for t in range(10):
                        bs.ask_price.append(get_value('i', data[i: i + 8]))
                        bs.ask_volume.append(get_value('q', data[i + 8:i + 24]))
                        i += 24
                    bs.msgseqid = get_msgseqid(data[i:i + 8])
                    # assert i != 688, 'length error:{0}'.format(data)
                    return bs
                elif type == '0c' and msgid == 2:
                    bs = bond_snap()
                    bs.sequence = data[2:10]
                    bs.exchange_id = data[10:12]
                    bs.securityid = get_value('9s', data[12:30])
                    bs.flag = data[30:34]
                    bs.tradingphasecode = data[34:50]
                    bs.instrumentstatus = get_value('6s', data[50:62])
                    bs.rsvd = data[62:64]
                    bs.timestamp = get_value('i', data[64:72])
                    bs.preclose_price = get_value('i', data[72:80])
                    bs.open_price = get_value('i', data[80:88])
                    bs.high_price = get_value('i', data[88:96])
                    bs.low_price = get_value('i', data[96:104])
                    bs.last_price = get_value('i', data[104:112])
                    bs.close_price = get_value('i', data[112:120])
                    bs.num_trades = get_value('i', data[120:128])
                    bs.total_volume_trade = get_value('q', data[128:144])
                    bs.total_value_trade = get_value('q', data[144:160])
                    bs.total_bid_qty = get_value('q', data[160:176])
                    bs.avg_bid_price = get_value('i', data[176:184])
                    bs.total_offer_qty = get_value('q', data[184:200])
                    bs.avg_offer_price = get_value('i', data[200:208])
                    bs.avg_price = get_value('i', data[208:216])
                    i = 216
                    if len(data) == 392 * 2:
                        bs.withDrawBuyNumber = get_value('i', data[216:224])
                        bs.withDrawBuyAmount = get_value('q', data[224:240])
                        bs.withDrawBuyAmount = get_value('q', data[240:256])
                        bs.withDrawSellNumber = get_value('i', data[256:264])
                        bs.withDrawSellAmount = get_value('q', data[264:280])
                        bs.withDrawSellAmount = get_value('q', data[280:296])
                        i = 296
                    for t in range(10):
                        bs.bid_price.append(get_value('i', data[i: i + 8]))
                        bs.bid_volume.append(get_value('q', data[i + 8:i + 24]))
                        i += 24
                    for t in range(10):
                        bs.ask_price.append(get_value('i', data[i: i + 8]))
                        bs.ask_volume.append(get_value('q', data[i + 8:i + 24]))
                        i += 24
                    bs.msgseqid = get_msgseqid(data[i:i + 8], 2)
                    # assert i != 688, 'length error:{0}'.format(data)
                    return bs
                elif type == '0d':
                    bt = bond_tick_by_tick()
                    bt.sequence = data[2:10]
                    bt.exchange_id = data[10:12]
                    bt.securityid = get_value('9s', data[12:30])
                    bt.tick_type = get_value('c', data[30:32])
                    bt.tickBSFlag = get_value('c', data[32:34])
                    bt.tick_index = get_value('i', data[34:42])
                    bt.channel = get_value('i', data[42:50])
                    bt.tick_time = get_value('i', data[50:58])
                    bt.buyorderno = get_value('q', data[58:74])
                    bt.sellorderno = get_value('q', data[74:90])
                    bt.price = get_value('i', data[90:98])
                    bt.qty = get_value('q', data[98:114])
                    bt.trade_money = get_value('q', data[114:130])
                    if msgid == 1:
                        bt.msgseqid = get_msgseqid(data[130:138])
                    elif msgid == 2:
                        bt.msgseqid = get_msgseqid(data[130:138], 2)
                    bt.rsvd = data[138:144]
                    return bt

            except Exception as e:
                print(data)
                print(e)
                return

    def write_new_file(self, md_time, str_hex):
        path = '/home/xiaoqingl/testdata/0603/'
        file_name = ''
        if str(md_time)[8:10] in ['09', '10', '13', '14']:
            file_name = 'fpga_' + str(md_time)[:11]
        else:
            file_name = 'fpga_' + str(md_time)[:10]
        if os.path.isfile(path + file_name):
            f = open(path + file_name, 'a')
            f.write(str_hex + '\n')
            f.close()
        else:
            f = open(path + file_name, 'w')
            f.write(str_hex + '\n')
            f.close()


if __name__ == '__main__':
    cu = CommUnpack()
    rst_file = '/home/xiaoqingl/fpga_0508.txt'
    fw = open(rst_file, 'w')
    fw.truncate()
    payload_file = '/home/xiaoqingl/outdata/sse/fpgano_0e_0508.txt'
    ss = '018cb40a0001363031383131000000ff0054313131000000005452414445000000000000e8700100302a0000a4010000d8ef100e00000000b820ee893b000000762a00004e2a000000000000762a0000302a000000000000000000000000000000000000c8290000a027a20e00000000fe2b000020950e140000000026000000485d92040000000068083051130000006e000000182d2a0900000000c0465a13270000006c2a000000350c0000000000622a000020df500000000000582a0000c0e1e400000000004e2a0000206de00000000000442a0000202f1401000000003a2a00008073060100000000302a0000a064d10100000000262a000040052801000000001c2a00000050c30000000000122a000020a1070000000000762a0000e03b660000000000802a00002052a600000000008a2a000060600b0200000000942a000000a86100000000009e2a0000808d5b0000000000a82a0000604d2f0000000000b22a000080584f0000000000bc2a0000e093040000000000c62a00000073550000000000d02a0000a0d6c4000000000028462300'
    rst = cu.unpack(ss, iswrite=0)
    print(rst)

    # with open(payload_file, 'r') as f:
    #     for line in f:
    #         rst = cu.unpack(line, iswrite = 0)
    #         if rst == None:
    #             print line
    #         fw.write(str(rst)+'\n')
    # fw.close()
