import os
import tushare as ts
from datasource.common import processSymbol


class Tushare:
    def __init__(self):
        self.tuCli = ts.pro_api(os.getenv("TUSHARETOKEN"))

    def StockList(self):
        return self.tuCli.stock_basic(
            exchange="",
            list_status="L",
            fields="ts_code,symbol,name,area,industry,list_date",
        )

    def GetDaily(self, symbol, start_date, end_date):
        return self.tuCli.daily(
            ts_code=processSymbol(symbol, source="tushare"),
            start_date=start_date,
            end_date=end_date,
        )

    def GetWeek(self, symbol, start_date, end_date):
        return self.tuCli.weekly(
            ts_code=processSymbol(symbol, source="tushare"),
            start_date=start_date,
            end_date=end_date,
            fields="ts_code,trade_date,open,high,low,close,vol,amount",
        )

    def GetMonth(self, symbol, start_date, end_date):
        return self.tuCli.monthly(
            ts_code=processSymbol(symbol, source="tushare"),
            start_date=start_date,
            end_date=end_date,
            fields="ts_code,trade_date,open,high,low,close,vol,amount",
        )
