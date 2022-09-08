from datetime import datetime
import akshare as ak


def IsTradeTime():
    openTime = datetime.now().replace(hour=0, minute=00, second=0, microsecond=0)
    closedTime = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    if openTime.hour <= datetime.now().hour <= closedTime.hour:
        return True
    return False


def GetHistoryData(symbol, start_date, end_date, period="daily"):
    return ak.stock_zh_a_hist(symbol=symbol, period=period,
                              start_date=start_date,
                              end_date=end_date, adjust="")
