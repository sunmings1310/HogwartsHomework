class Snap:
    def __init__(self):
        self.type = '01'
        self.sequence = 0
        self.exchange_id = '01'
        self.securityid = ''
        self.flag = ''
        self.tradingphasecode = ''
        self.instrumentStatus = '0'
        self.timestamp = ''
        self.preclose_price = ''
        self.numtrades = ''
        self.totalvolumetrade = ''
        self.totalvaluetrade = ''
        self.last_price = ''
        self.open_price = ''
        self.close_price = '0'
        self.high_price = ''
        self.low_price = ''
        self.upperlmt_price = ''
        self.lowerlmt_price = ''
        self.bid_avg_price = ''
        self.bid_total_qty = ''
        self.ask_avg_price = ''
        self.ask_total_qty = ''
        self.bid_price_list = []
        self.bid_vol_list = []
        self.ask_price_list = []
        self.ask_vol_list = []
        self.msgSeqId = '0' * 8
        self.withDrawBuyNumber = ''
        self.withDrawBuyAmount = ''
        self.withDrawBuyMoney = ''
        self.withDrawSellNumber = ''
        self.withDrawSellAmount = ''
        self.withDrawSellMoney = ''

    def __repr__(self):
        return 'type=' + str(self.type).ljust(4, ' ') + 'sequence=' + str(self.sequence).ljust(10, ' ') + 'exchange_id=' + str(self.exchange_id).ljust(4, ' ') + 'securityid=' + str(self.securityid).ljust(10, ' ') + 'flag=' + str(self.flag).ljust(8, ' ') + \
               'tradingphasecode=' + str(self.tradingphasecode).ljust(8, ' ') + 'instrumentStatus=' + str(self.instrumentStatus).ljust(6, ' ') + 'timestamp=' + str(self.timestamp).ljust(18, ' ') + 'preclose_price=' + str(self.preclose_price).ljust(20, ' ') + \
               'numtrades=' + str(self.numtrades).ljust(20, ' ') + 'totalvolumetrade=' + str(self.totalvolumetrade).ljust(20, ' ') + 'toalvaluetrade=' + str(self.totalvaluetrade).ljust(20, ' ') + 'last_price=' + str(self.last_price).ljust(20, ' ') + \
               'open_price=' + str(self.open_price).ljust(20, ' ') + 'close_price=' + str(self.close_price).ljust(20, ' ') + 'high_price=' + str(self.high_price).ljust(20, ' ') + 'low_price=' + str(self.low_price).ljust(20, ' ') +\
               'upperlmt_price=' + str(self.upperlmt_price).ljust(20, ' ') + 'lowerlmt_price=' + str(self.lowerlmt_price).ljust(20, ' ') + 'bid_avg_price=' + str(self.bid_avg_price).ljust(20, ' ') + 'bid_total_qty=' + str(self.bid_total_qty).ljust(20, ' ') +\
               'ask_avg_price=' + str(self.ask_avg_price).ljust(20, ' ') + 'ask_total_qty=' + str(self.ask_total_qty).ljust(20, ' ') + 'bid_price_list=' + str(self.bid_price_list).ljust(80, ' ') + 'bid_vol_list=' + str(self.bid_vol_list).ljust(80, ' ') + \
               'ask_price_list=' + str(self.ask_price_list).ljust(80, ' ') + 'ask_vol_list=' + str(self.ask_vol_list).ljust(80, ' ') + 'msgSeqId=' + str(self.msgSeqId).ljust(8, ' ')
               #+ 'sendingTime=' + str(self.sendingTime)

class Tick_Total_5803:
    def __init__(self):
        self.type = '11'
        self.sequence = 0
        self.exchange_id = '01'
        self.securityid = ''
        self.TickType = ''
        self.TickBSFlag = ''
        self.Tickindex = ''
        self.Channel = ''
        self.TickTime = ''
        self.BuyOrderNo = ''
        self.SellOrderNo = ''
        self.Price = ''
        self.Qty = ''
        self.TradeMoney = ''
        self.MsgSeqId = ''
        self.Rsvd = ''

    def __repr__(self):
        return 'type=' + str(self.type).ljust(4, ' ') + 'sequence=' + str(self.sequence).ljust(10, ' ') + 'exchange_id=' + str(self.exchange_id).ljust(4, ' ') + 'securityid=' + str(self.securityid).ljust(10, ' ') +\
               'TickType='  + str(self.TickType).ljust(4, ' ') + 'TickBSFlag='  + str(self.TickBSFlag).ljust(4, ' ') + 'Tickindex='  + str(self.Tickindex).ljust(10, ' ') + 'Channel='  + str(self.Channel).ljust(6, ' ') +\
               'TickTime='  + str(self.TickTime).ljust(10, ' ') + 'BuyOrderNo='  + str(self.BuyOrderNo).ljust(10, ' ') + 'SellOrderNo='  + str(self.SellOrderNo).ljust(10, ' ') + 'Price='  + str(self.Price).ljust(15, ' ') +\
               'Qty='  + str(self.Qty).ljust(15, ' ') + 'TradeMoney='  + str(self.TradeMoney).ljust(15, ' ') + 'MsgSeqID='  + str(self.MsgSeqId).ljust(8, ' ')

class ETF_1502:
    def __init__(self):
        self.type = '10'
        self.sequence = 0
        self.exchange_id = '01'
        self.securityid = ''
        self.TimeStamp = ''
        self.ETFBuyNumber = ''
        self.ETFBuyAmount = ''
        self.ETFBuyMoney = ''
        self.ETFSellNumber = ''
        self.ETFSellAmount = ''
        self.ETFSellMoney = ''
        self.MsgSeqId = ''
        self.Rsvd = ''
    def __repr__(self):
        return 'type=' + str(self.type).ljust(4, ' ') + 'sequence=' + str(self.sequence).ljust(10, ' ') + 'exchange_id=' + str(self.exchange_id).ljust(4, ' ') + 'securityid=' + str(self.securityid).ljust(10, ' ') +\
        'TimeStamp=' + str(self.TimeStamp).ljust(10, ' ') + 'ETFBuyNumber=' + str(self.ETFBuyNumber).ljust(10, ' ') + 'ETFBuyAmount=' + str(self.ETFBuyAmount).ljust(10, ' ') +\
        'ETFBuyMoney=' + str(self.ETFBuyMoney).ljust(15, ' ') + 'ETFSellNumber=' + str(self.ETFSellNumber).ljust(10, ' ') + 'ETFSellAmount=' + str(self.ETFSellAmount).ljust(10, ' ') +\
        'ETFSellMoney=' + str(self.ETFSellMoney).ljust(15, ' ') + 'MsgSeqID=' + str(self.MsgSeqId).ljust(8, ' ')


class Orders:
    def __init__(self):
        self.type = '02'
        self.sequence = 0
        self.exchange_id = '01'
        self.securityid = ''
        self.timestamp = ''
        self.side = ''
        self.price = ''
        self.qty = ''
        self.order_numbers = ''
        self.volume_list = []
        self.channelno = '0'
        self.mdstreamid = '0'*6
        self.msgSeqId = '0' * 8

    def __repr__(self):
        return 'type=' + str(self.type).ljust(4, ' ') + 'sequence=' + str(self.sequence).ljust(10, ' ') + 'exchange_id=' + str(self.exchange_id).ljust(4, ' ') + 'securityid=' + str(self.securityid).ljust(10, ' ') + \
                'timestamp=' + str(self.timestamp).ljust(18, ' ') + 'side=' + str(self.side).ljust(2, ' ') + 'price=' + str(self.price).ljust(18, ' ') + 'qty=' + str(self.qty).ljust(18, ' ') + 'order_numbers=' + str(self.order_numbers).ljust(4, ' ') + \
                'volume_list=' + str(self.volume_list).ljust(400, ' ') + 'channelno=' + str(self.channelno).ljust(6, ' ') + 'mdstreamid=' + str(self.mdstreamid).ljust(6, ' ') + 'msgSeqId=' + str(self.msgSeqId).ljust(8, ' ') #+ 'sendingTime=' + str(self.sendingTime)


class IndexMd:
    def __init__(self):
        self.type = '03'
        self.sequence = 0
        self.exchange_id = '01'
        self.securityid = ''
        self.flag = ''
        self.timestamp = ''
        self.tradeTime = '0'
        self.preclose_price = ''
        self.open_price = ''
        self.last_price = ''
        self.high_price = ''
        self.low_price = ''
        self.closeIndex = ''
        self.total_volume = ''
        self.total_value = ''
        self.msgSeqId = '0'*8

    def __repr__(self):
        return 'type=' + str(self.type).ljust(4, ' ') + 'sequence=' + str(self.sequence).ljust(10, ' ') + 'exchange_id=' + str(self.exchange_id).ljust(4, ' ') + 'securityid=' + str(self.securityid).ljust(10, ' ') + \
               'flag=' + str(self.flag).ljust(5, ' ') + 'timestamp=' + str(self.timestamp).ljust(18, ' ') + 'tradeTime=' + str(self.tradeTime).ljust(18, ' ') + \
               'preclose_price=' + str(self.preclose_price).ljust(18, ' ') + 'open_price=' + str(self.open_price).ljust(18, ' ') + 'last_price=' + str(self.last_price).ljust(18, ' ') + 'high_price=' + str(self.high_price).ljust(18, ' ') + \
               'low_price=' + str(self.low_price).ljust(18,' ') + 'closeIndex=' + str(self.closeIndex).ljust(18,' ') +'total_volume=' + str(self.total_volume).ljust(18,' ') + \
               'total_value=' + str(self.total_value).ljust(6, ' ') + 'msgSeqId=' + str(self.msgSeqId).ljust(8, ' ')


class TradeByLine:
    def __init__(self):
        self.type = '04'
        self.sequence = 0
        self.exchange_id = '01'
        self.TradeBSFlag = '00'
        self.msgSeqId = '0' * 8
        self.applseqnum = ''
        self.securityid = ''
        self.channelno = '0'
        self.transacttime = ''
        self.tradePrice = ''
        self.tradeQty = ''
        self.trademoney = '0'
        self.tradeBuyNo = ''
        self.tradeSellNo = ''
        self.bizIndex = ''

    def __repr__(self):
        return 'type=' + str(self.type).ljust(4, ' ') + 'sequence=' + str(self.sequence).ljust(10,' ') +\
               'exchange_id=' + str(self.exchange_id).ljust(4, ' ') + 'securityid=' + str(self.securityid).ljust(10, ' ') + \
                'TradeBSFlag=' + str(self.TradeBSFlag).ljust(4, ' ') + 'applseqnum=' + str(self.applseqnum).ljust(10, ' ') + \
               'transacttime=' + str(self.transacttime).ljust(18, ' ') + \
               'tradePrice=' + str(self.tradePrice).ljust(18, ' ') + 'tradeQty=' + str(self.tradeQty).ljust(18,' ') + \
               'trademoney=' + str(self.trademoney).ljust(18, ' ') + 'tradeBuyNo=' + str(self.tradeBuyNo).ljust(18, ' ') + \
               'tradeSellNo=' + str(self.tradeSellNo).ljust(20, ' ') + 'channelno=' + str(self.channelno).ljust(6, ' ') + \
               'msgSeqId=' + str(self.msgSeqId).ljust(10, ' ') + 'bizIndex=' + str(self.bizIndex)


class TradeByLineOld:
    def __init__(self):
        self.type = '04'
        self.sequence = 0
        self.exchange_id = '01'
        self.securityid = ''
        self.exec_type = '02'
        self.TradeBSFlag = '00'
        self.applseqnum = ''
        self.transacttime = ''
        self.tradePrice = ''
        self.tradeQty = ''
        self.trademoney = '0'
        self.tradeBuyNo = ''
        self.tradeSellNo = ''
        self.channelno = '0'
        self.mdstreamid = '0'*6
        self.msgSeqId = '0' * 8
        self.sendingTime = '0' * 12

    def __repr__(self):
        return 'type=' + str(self.type).ljust(4, ' ') + 'sequence=' + str(self.sequence).ljust(10, ' ') + 'exchange_id=' + str(self.exchange_id).ljust(4, ' ') + 'securityid=' + str(self.securityid).ljust(10, ' ') + \
               'exec_type=' + str(self.exec_type).ljust(4, ' ') + 'TradeBSFlag=' + str(self.TradeBSFlag).ljust(4, ' ') + 'applseqnum=' + str(self.applseqnum).ljust(10, ' ') + 'transacttime=' + str(self.transacttime).ljust(18, ' ') + \
               'tradePrice=' + str(self.tradePrice).ljust(18, ' ') + 'tradeQty=' + str(self.tradeQty).ljust(18, ' ') + 'trademoney=' + str(self.trademoney).ljust(18, ' ') + 'tradeBuyNo=' + str(self.tradeBuyNo).ljust(18, ' ') + \
               'tradeSellNo=' + str(self.tradeSellNo).ljust(20, ' ') + 'channelno=' + str(self.channelno).ljust(6, ' ') + 'mdstreamid=' + str(self.mdstreamid).ljust(8,' ') + 'msgSeqId=' + str(self.msgSeqId).ljust(10, ' ') + 'sendingTime=' + str(self.sendingTime)


class EntrustByLine: #5801
    def __init__(self):
        self.type = '05'
        self.sequence = 0
        self.exchange_id = '01'
        self.securityid = ''
        self.orderBSFlag = ''
        self.orderType = ''
        self.orderIndex = ''
        self.orderTime = ''
        self.orderNo = ''
        self.orderPrice = ''
        self.balance = ''
        self.channelno = '0' * 8
        self.bizIndex = ''
        self.msgSeqId = ''

    def __repr__(self):
        return 'type=' + str(self.type).ljust(4, ' ') + 'sequence=' + str(self.sequence).ljust(10, ' ') + 'exchange_id=' + str(self.exchange_id).ljust(4, ' ') + 'securityid=' + str(self.securityid).ljust(10, ' ') +\
                'orderType=' + str(self.orderType).ljust(4, ' ') + 'orderBSFlag=' + str(self.orderBSFlag).ljust(4, ' ') + 'orderIndex=' + str(self.orderIndex).ljust(18, ' ') + 'orderTime=' + str(self.orderTime).ljust(18, ' ') + \
                'orderNo=' + str(self.orderNo).ljust(18, ' ') + 'orderPrice=' + str(self.orderPrice).ljust(18, ' ') +'channelno=' + str(self.channelno).ljust(6, ' ') + 'balance=' + str(self.balance).ljust(18, ' ') + \
               'bizIndex=' + str(self.bizIndex).ljust(18, ' ') + 'msgSeqId=' + str(self.msgSeqId).ljust(18, ' ')


class TradeEndOfDay3108:
    def __init__(self):
        self.type = '07'
        self.sequence = ''
        self.exchange_id = '01'
        self.securityid = ''
        self.flag = ''
        self.instrumentStatus = ''
        self.datatimeStamp = ''
        self.closePx = ''
        self.numTrades = ''
        self.totalVolumeTrade = ''
        self.totalValueTrade = ''
        self.totalBidQty = ''
        self.totalSellQty = ''
        self.withDrawBuyNumber = ''
        self.withDrawBuyAmount = ''
        self.withDrawSellNumber = ''
        self.withDrawSellAmount = ''
        self.noBidLevel = ''
        self.noOfferLevel = ''
        self.bidOrderQty = ''
        self.askOrderQty = ''
        self.bidNoOrders = ''
        self.askNoOrders = ''
        self.bidOrderQty50 = []
        self.askOrderQty50 = []
        self.msgSeqID = ''

    def __repr__(self):
        type = 'type={0} '.format(self.type).ljust(4, ' ')
        sequence = 'sequence={0} '.format(self.sequence).ljust(10, ' ')
        exchange_id = 'exchange_id={0} '.format(self.exchange_id).ljust(4, ' ')
        securityID = 'securityID={0} '.format(self.securityid).ljust(10, ' ')
        flag = 'flag={0} '.format(self.flag).ljust(8, ' ')
        instrumentStatus = 'instrumentStatus={0} '.format(self.instrumentStatus).ljust(8, ' ')
        datatimeStamp = 'datatimeStamp={0} '.format(self.datatimeStamp).ljust(12, ' ')
        closePx = 'closePx={0} '.format(self.closePx).ljust(15, ' ')
        numTrades = 'numTrades={0} '.format(self.numTrades).ljust(15, ' ')
        totalVolumeTrade = 'totalVolumeTrade={0} '.format(self.totalVolumeTrade).ljust(15, ' ')
        totalValueTrade = 'totalValueTrade={0} '.format(self.totalValueTrade).ljust(15, ' ')
        totalBidQty = 'totalBidQty={0} '.format(self.totalBidQty).ljust(15, ' ')
        totalSellQty = 'totalSellQty={0} '.format(self.totalSellQty).ljust(15, ' ')
        withDrawBuyNumber = 'withDrawBuyNumber={0} '.format(self.withDrawBuyNumber).ljust(15, ' ')
        withDrawBuyAmount = 'withDrawBuyAmount={0} '.format(self.withDrawBuyAmount).ljust(15, ' ')
        withDrawSellNumber = 'withDrawSellNumber={0} '.format(self.withDrawSellNumber).ljust(15, ' ')
        withDrawSellAmount = 'withDrawSellAmount={0} '.format(self.withDrawSellAmount).ljust(15, ' ')
        noBidLevel = 'noBidLevel={0} '.format(self.noBidLevel).ljust(10, ' ')
        noOfferLevel = 'noOfferLevel={0} '.format(self.noOfferLevel).ljust(10, ' ')
        bidOrderQty = 'bidOrderQty={0} '.format(str(self.bidOrderQty)).ljust(10, ' ')
        askOrderQty = 'askOrderQty={0} '.format(str(self.askOrderQty)).ljust(10, ' ')
        bidNoOrders = 'bidNoOrders={0} '.format(self.bidNoOrders).ljust(15, ' ')
        askNoOrders = 'askNoOrders={0} '.format(self.askNoOrders).ljust(15, ' ')
        bidOrderQty50 = 'bidOrderQty50={0} '.format(str(self.bidOrderQty50)).ljust(len(self.bidOrderQty50)*15, ' ')
        askOrderQty50 = 'askOrderQty50={0} '.format(str(self.askOrderQty50)).ljust(len(self.bidOrderQty50)*15, ' ')
        msgSeqID = 'msgSeqID={0} '.format(self.msgSeqID).ljust(10, ' ')

        return type+sequence+exchange_id+securityID+flag+instrumentStatus+datatimeStamp+closePx+numTrades+totalVolumeTrade+totalValueTrade+totalBidQty+\
               totalSellQty+withDrawBuyNumber+withDrawBuyAmount+withDrawSellNumber+withDrawSellAmount+noBidLevel+noOfferLevel+bidOrderQty+askOrderQty+\
               bidNoOrders+askNoOrders+bidOrderQty50+askOrderQty50+msgSeqID#+sendingTime


class MktData3209:
    def __init__(self):
        self.type = '08'
        self.sequence = ''
        self.exchange_id = '01'
        self.securityid = ''
        self.tradeBSFlag = '00'
        self.tradeindex = ''
        self.tradeTime = ''
        self.tradeprice = ''
        self.tradeqty = ''
        self.trademoney = '0'
        self.tradebuyno = ''
        self.tradesellno = ''
        self.channelno = '0'
        self.msgSeqID = '0' * 8

    def __repr__(self):
        type = 'type={0}  '.format(self.type).ljust(4, ' ')
        sequence = 'sequence={0}  '.format(self.sequence).ljust(8, ' ')
        exchange_id = 'exchange_id={0}  '.format(self.exchange_id).ljust(4, ' ')
        securityid = 'securityid={0}  '.format(self.securityid).ljust(10, ' ')
        tradeBSFlag = 'tradeBSFlag={0}  '.format(self.tradeBSFlag).ljust(4, ' ')
        tradeindex = 'tradeindex={0}  '.format(self.tradeindex).ljust(15, ' ')
        transacttime = 'tradeTime={0}  '.format(self.tradeTime).ljust(15, ' ')
        tradeprice = 'tradeprice={0}  '.format(self.tradeprice).ljust(15, ' ')
        tradeqty = 'tradeqty={0}  '.format(self.tradeqty).ljust(15, ' ')
        trademoney = 'trademoney={0}  '.format(self.trademoney).ljust(15, ' ')
        tradebuyno = 'tradebuyno={0}  '.format(self.tradebuyno).ljust(15, ' ')
        tradesellno = 'tradesellno={0}  '.format(self.tradesellno).ljust(15, ' ')
        channelno = 'channelno={0}  '.format(self.channelno).ljust(6, ' ')
        msgSeqID = 'msgSeqID={0}  '.format(self.msgSeqID).ljust(10, ' ')

        return type+sequence+exchange_id+securityid+tradeBSFlag+tradeindex+transacttime+tradeprice+\
               tradeqty+trademoney+tradebuyno+tradesellno+channelno+msgSeqID


class OptionLv1:
    def __init__(self):
        self.type = '0e'
        self.sequence = ''
        self.exchange_id = '01'
        self.securityid = ''
        self.tradeVolume = ''
        self.totalValueTraded = ''
        self.totalLongPosition = ''
        self.preClosePrice = ''
        self.prevSetPrice = ''
        self.tradePrice = ''
        self.openPrice = ''
        self.closePrice = ''
        self.settlePrice = ''
        self.highPrice = ''
        self.lowPrice = ''
        self.auctionPrice = ''
        self.auctionQty = ''
        self.tradingPhaseCode = ''
        self.bidPrice = []
        self.bidVolume = []
        self.askPrice = []
        self.askVolume = []
        self.msgseqid = ''
        self.uptimeStamp_s = ''
        self.uptimeStamp_ms = ''

    def __repr__(self):
        type = 'type={0}  '.format(self.type).ljust(4, ' ')
        sequence = 'sequence={0}  '.format(self.sequence).ljust(8, ' ')
        exchange_id = 'exchange_id={0}  '.format(self.exchange_id).ljust(4, ' ')
        securityid = 'securityid={0}  '.format(self.securityid).ljust(10, ' ')
        tradeVolume = 'tradeVolume={0}  '.format(self.tradeVolume).ljust(4, ' ')
        totalValueTraded = 'totalValueTraded={0}  '.format(self.totalValueTraded).ljust(4, ' ')
        totalLongPosition = 'totalLongPosition={0}  '.format(self.totalLongPosition).ljust(15, ' ')
        preClosePrice = 'preClosePrice={0}  '.format(self.preClosePrice).ljust(15, ' ')
        prevSetPrice = 'prevSetPrice={0}  '.format(self.prevSetPrice).ljust(15, ' ')
        tradePrice = 'tradePrice={0}  '.format(self.tradePrice).ljust(15, ' ')
        openPrice = 'openPrice={0}  '.format(self.openPrice).ljust(15, ' ')
        closePrice = 'closePrice={0}  '.format(self.closePrice).ljust(15, ' ')
        settlePrice = 'settlePrice={0}  '.format(self.settlePrice).ljust(15, ' ')
        highPrice = 'highPrice={0}  '.format(self.highPrice).ljust(15, ' ')
        lowPrice = 'lowPrice={0}  '.format(self.lowPrice).ljust(15, ' ')
        auctionPrice = 'auctionPrice={0}  '.format(self.auctionPrice).ljust(15, ' ')
        auctionQty = 'auctionQty={0}  '.format(self.auctionQty).ljust(15, ' ')
        tradingPhaseCode = 'tradingPhaseCode={0}  '.format(self.tradingPhaseCode).ljust(15, ' ')
        bidPrice = 'bidPrice={0}  '.format(str(self.bidPrice)).ljust(15*len(self.bidPrice), ' ')
        bidVolume = 'bidVolume={0}  '.format(str(self.bidVolume)).ljust(15*len(self.bidVolume), ' ')
        askPrice = 'askPrice={0}  '.format(str(self.askPrice)).ljust(4*len(self.askPrice), ' ')
        askVolume = 'askVolume={0}  '.format(str(self.askVolume)).ljust(4*len(self.askVolume), ' ')
        msgseqid = 'msgseqid={0}  '.format(self.msgseqid).ljust(10, ' ')
        uptimeStamp = 'uptimeStamp_s={0}  '.format(self.uptimeStamp_s).ljust(12, ' ')
        uptimeStamp_ms = 'uptimeStamp_ms={0}  '.format(self.uptimeStamp_ms).ljust(12, ' ')

        return type+exchange_id+securityid+sequence+tradeVolume+totalValueTraded+totalLongPosition+preClosePrice+prevSetPrice+tradePrice+openPrice+\
               closePrice+settlePrice+highPrice+lowPrice+auctionPrice+auctionQty+tradingPhaseCode+bidPrice+bidVolume+askPrice+askVolume+uptimeStamp+uptimeStamp_ms+msgseqid


class bond_snap:
    def __init__(self):
        self.type = '0c'
        self.sequence = ''
        self.exchange_id = '01'
        self.securityid = ''
        self.flag = ''
        self.tradingphasecode = ''
        self.instrumentstatus = ''
        self.rsvd = ''
        self.timestamp = ' '
        self.preclose_price = ''
        self.open_price = ''
        self.high_price = ''
        self.low_price = ''
        self.last_price = ''
        self.close_price = ''
        self.num_trades = ''
        self.total_volume_trade = ''
        self.total_value_trade = ''
        self.total_bid_qty = ''
        self.avg_bid_price = ''
        self.total_offer_qty = ''
        self.avg_offer_price = ''
        self.avg_price = ''
        self.bid_price = []
        self.bid_volume = []
        self.ask_price = []
        self.ask_volume = []
        self.msgseqid = ''
        self.withDrawBuyNumber = ''
        self.withDrawBuyAmount = ''
        self.withDrawBuyMoney = ''
        self.withDrawSellNumber = ''
        self.withDrawSellAmount = ''
        self.withDrawSellMoney = ''


class bond_tick_by_tick:
    def __init__(self):
        self.type = '0d'
        self.sequence = ''
        self.exchange_id = '01'
        self.securityid = ''
        self.tick_type = ''
        self.tickBSFlag = ''
        self.tick_index = ''
        self.channel = ''
        self.tick_time = ''
        self.buyorderno = ''
        self.sellorderno = ''
        self.price = ''
        self.qty = ''
        self.trade_money = ''
        self.msgseqid = ''
        self.rsvd = ''
