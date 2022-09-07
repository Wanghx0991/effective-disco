import requests
from datetime import datetime
from dateutil import parser
from time import sleep


class Tick:
    def __init__(self, code):
        self.vol = None
        self.trade_datetime = None
        self.last = None
        self.low = None
        self.high = None
        self.started = None
        self.closed = None
        self.code = code
        if self.code.startswith('6'):
            self.code = 'sh' + self.code
        elif self.code.startswith('0'):
            self.code = 'sz' + self.code

        self.Tencent = 'https://qt.gtimg.cn/q='

    def GetTick(self):
        resp = requests.get(self.Tencent + self.code).text
        raw = resp.split("~")
        self.low, self.high = float(raw[34]), float(raw[33])
        self.started, self.closed = float(raw[5]), float(raw[3])
        self.last = float(raw[3])
        self.trade_datetime = parser.parse(raw[30])
        self.vol = int(raw[6])
        return self.closed,self.trade_datetime


if __name__ == '__main__':
    tickObj = Tick('600036')
    openTime = datetime.now().replace( hour=9, minute=30, second=0, microsecond=0 )
    closedTime = datetime.now().replace( hour=23, minute=59, second=0, microsecond=0 )
    while openTime.hour <= datetime.now().hour <= closedTime.hour:
        res,tim = tickObj.GetTick()
        print('code = %s, price = %d, tim = %s' % (tickObj.code,res,tim))
        sleep(3)

