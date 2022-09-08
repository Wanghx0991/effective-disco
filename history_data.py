import os
import tushare as ts

# 8e786e496bbde5d457515033f79242d2f564b29fb7b559e7f45c4fc0


class Tushare:
    def __init__(self):
        self.tuCli = ts.pro_api(os.getenv('TUSHARETOKEN'))

    def GetDaily(self,symbol,start_date,end_date):
        self.tuCli.daily()




