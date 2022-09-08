import requests
from stock import IsTradeTime
from dateutil import parser
from time import sleep
import logging

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)


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
        self.symbol = symbol
        if self.symbol.startswith('6'):
            self.symbol = 'sh' + self.symbol
        elif self.symbol.startswith('0'):
            self.symbol = 'sz' + self.symbol

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
        started, closed = [], []
        tick.getTick()
        started.append(tick.started)
        closed.append(tick.closed)
        logging.info(
            'code = %s, price = %f, tim = %s, started = %f, vol = %d' % (tick.symbol, tick.closed, tick.trade_datetime,
                                                                         tick.started, tick.last_volume))
        sleep(5)
