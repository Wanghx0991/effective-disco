from logger import *
from stock import *
import requests
from time import sleep
from dateutil import parser


class Tick:
    Tencent = 'https://qt.gtimg.cn/q='

    def __init__(self, symbol):
        self.last_volume = None  # 瞬时成交量
        self.last_amount = None  # 瞬时成交额
        self.cum_volume = None  # 成交总量
        self.cum_amount = None  # 成交总额
        self.trade_datetime = None
        self.last = None
        self.low = None
        self.high = None
        self.started = None
        self.closed = None
        self.symbol = processSymbol(symbol)

    def getTick(self):
        resp = requests.get(self.Tencent + self.symbol).text
        raw = resp.split("~")
        self.low, self.high = float(raw[34]), float(raw[33])
        self.started, self.closed = float(raw[5]), float(raw[3])
        self.last = float(raw[3])
        self.trade_datetime = parser.parse(raw[30])
        self.last_volume = int(raw[6])


if __name__ == '__main__':
    tick = Tick('600036')
    while IsTradeTime():
        tick.getTick()
        # print('code = %s, price = %f, trade_time = %s, started = %f, vol = %d' % (tick.symbol, tick.closed,
        # tick.trade_datetime, tick.started, tick.last_volume))
        logger.info(
            'code = %s, price = %f, trade_time = %s, started = %f, vol = %d' % (
                tick.symbol, tick.closed, tick.trade_datetime,
                tick.started, tick.last_volume)
        )
        sleep(2)
