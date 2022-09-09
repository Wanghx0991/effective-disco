import os
import tushare as ts
import akshare as ak
from datetime import datetime


def IsTradeTime():
    openTime = datetime.now().replace(hour=0, minute=00, second=0, microsecond=0)
    closedTime = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    if openTime.hour <= datetime.now().hour <= closedTime.hour:
        return True
    return False


def processSymbol(symbol, source='Tencent'):
    symbol_processed = ""
    if source == 'tushare':
        if symbol.startswith('6'):
            symbol_processed = symbol + ".SH"
        elif symbol.startswith('0'):
            symbol_processed = symbol + ".SZ"
        elif symbol.startswith('8'):
            symbol_processed = symbol + ".BJ"
    elif source == 'Tencent':
        if symbol.startswith('6'):
            symbol_processed = 'sh' + symbol
        elif symbol.startswith('0'):
            symbol_processed = 'sz' + symbol
    return symbol_processed


class Tushare:
    def __init__(self):
        self.tuCli = ts.pro_api(os.getenv('TUSHARETOKEN'))

    def StockList(self):
        return self.tuCli.stock_basic(exchange='', list_status='L',
                                      fields='ts_code,symbol,name,area,industry,list_date')

    def GetDaily(self, symbol, start_date, end_date):
        return self.tuCli.daily(ts_code=processSymbol(symbol, source='tushare'), start_date=start_date,
                                end_date=end_date)

    def GetWeek(self, symbol, start_date, end_date):
        return self.tuCli.weekly(ts_code=processSymbol(symbol, source='tushare'), start_date=start_date,
                                 end_date=end_date,
                                 fields='ts_code,trade_date,open,high,low,close,vol,amount')

    def GetMonth(self, symbol, start_date, end_date):
        return self.tuCli.monthly(ts_code=processSymbol(symbol, source='tushare'), start_date=start_date,
                                  end_date=end_date,
                                  fields='ts_code,trade_date,open,high,low,close,vol,amount')


class Akshare:
    # 单支股票的历史行情数据
    # 历史行情数据-东财
    # 目标地址: http: //quote.eastmoney.com / concept / sh603777.html?from=classic(示例)
    # 描述: 东方财富 - 沪深京A股日频率数据;历史数据按日频率更新, 当日收盘价请在收盘后获取
    # 限量: 单次返回指定沪深京A股上市公司、指定周期和指定日期间的历史行情日频率数据
    def stock_zh_a_hist(self, symbol, start_date, end_date, freq='daily', adjust=''):
        if freq not in ['daily', 'weekly', 'monthly']:
            raise "please input the correct the frequency: {'daily', 'weekly', 'monthly'}"
        data = ak.stock_zh_a_hist(symbol=symbol, period=freq, start_date=start_date, end_date=end_date)
        data.columns = ['date', 'open', 'close', 'high', 'low', 'volume', 'amount', 'amplitude', 'quote_change',
                        'ups_downs', 'turnover']
        return data

    # 单只股票的分时图
    # 描述: 东方财富网-行情首页-沪深京 A 股-每日分时行情; 该接口只能获取近期的分时数据，注意时间周期的设置
    # 限量: 单次返回指定股票、频率、复权调整和时间区间的分时数据, 其中 1 分钟数据只返回近 5 个交易日数据且不复权
    def stock_zh_a_hist_min_em(self, symbol, start_date, end_date, freq='5', ):
        if freq not in ['1', '5', '15', '30', '60']:
            raise "please input the correct the frequency: {'1', '5', '15', '30', '60'}"

        return ak.stock_zh_a_hist_min_em(symbol=symbol, start_date=start_date, end_date=end_date, period='5', adjust='')

    # 东方财富网-沪深京 A 股-实时行情数据
    # 限量: 单次返回所有沪深京 A 股上市公司的实时行情数据
    def stock_zh_a_spot_em(self):
        return ak.stock_zh_a_spot_em()


if __name__ == '__main__':
    # cli = Tushare()
    # objDaily = cli.GetDaily('600036', '20220501', '20220701')
    # objWeek = cli.GetWeek('600036', '20220501', '20220701')
    # objMonth = cli.GetMonth('600036', '20220501', '20220701')
    # stockList = cli.StockList()

    cli = Akshare()
    # resp = cli.stock_zh_a_hist('600036', '20220501', '20220701')
    # resp2 = cli.stock_zh_a_hist_min_em('600036', '20220908', '20220908')
    resp3 = cli.stock_zh_a_spot_em()
    pass
