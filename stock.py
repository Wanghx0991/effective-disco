from datetime import datetime
import akshare as ak
import tushare as ts


def IsTradeTime():
    openTime = datetime.now().replace(hour=0, minute=00, second=0, microsecond=0)
    closedTime = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    if openTime.hour <= datetime.now().hour <= closedTime.hour:
        return True
    return False


def GetAkHistoryData(symbol, start_date, end_date, period="daily"):
    return ak.stock_zh_a_hist(symbol=symbol, period=period,
                              start_date=start_date,
                              end_date=end_date, adjust="")


def processSymbol(symbol, source='Tencent'):
    symbol_processed = ""
    if source == 'akshare':
        pass
    elif source == 'tushare':
        pass
    elif source == 'Tencent':
        if symbol.startswith('6'):
            symbol_processed = 'sh' + symbol
        elif symbol.startswith('0'):
            symbol_processed = 'sz' + symbol

    return symbol_processed
