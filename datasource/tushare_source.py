import os
import tushare as ts
import pandas as pd
import json
from datasource.common import processSymbol


class Tushare:
    def __init__(self):
        self.tuCli = ts.pro_api(os.getenv("TUSHARETOKEN"))

    # 查询当前所有正常上市交易的股票列表
    def StockList(self,exchange = 'sh+sz'):
        if exchange == 'sh':
            return self.tuCli.stock_basic(
                exchange="SSE",
                list_status="L",
                fields="ts_code,symbol,name,area,industry,list_date",
            )
        elif exchange == 'sz':
            return self.tuCli.stock_basic(
                exchange="SZSE",
                list_status="L",
                fields="ts_code,symbol,name,area,industry,list_date",
            )
        elif exchange == 'sh+sz':
            sh = self.tuCli.stock_basic(
                exchange="SSE",
                list_status="L",
                fields="ts_code,symbol,name,area,industry,list_date",
            )
            sz = self.tuCli.stock_basic(
                exchange="SZSE",
                list_status="L",
                fields="ts_code,symbol,name,area,industry,list_date",
            )
            return pd.concat([sh,sz])
        elif exchange == 'all':
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


if __name__ == '__main__':
    cli = Tushare()
    data = cli.StockList(exchange='sh+sz').to_csv('../stock_list.csv',index=False)

