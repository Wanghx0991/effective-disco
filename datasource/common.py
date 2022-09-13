from datetime import datetime


def IsTradeTime():
    openTime = datetime.now().replace(hour=0, minute=00, second=0, microsecond=0)
    closedTime = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    if openTime.hour <= datetime.now().hour <= closedTime.hour:
        return True
    return False


def processSymbol(symbol, source="Tencent"):
    symbol_processed = ""
    if source == "tushare":
        if symbol.startswith("6"):
            symbol_processed = symbol + ".SH"
        elif symbol.startswith("0"):
            symbol_processed = symbol + ".SZ"
        elif symbol.startswith("8"):
            symbol_processed = symbol + ".BJ"
    elif source == "Tencent":
        if symbol.startswith("6"):
            symbol_processed = "sh" + symbol
        elif symbol.startswith("0"):
            symbol_processed = "sz" + symbol
    return symbol_processed
