import pandas as pd
import pandas_ta as ta


def is_metric_exist(metric):
    CurrentMetric = pd.DataFrame().ta.indicators(as_list=True)
    if metric in CurrentMetric:
        return True
    return False


def is_pattern_exist(pattern):
    CurrentPattern = ta.ALL_PATTERNS
    if pattern in CurrentPattern:
        return True
    return False


def vwap(data):
    ret = data.ta.vwap(append=True)
    data.rename(columns={"VWAP_D": "vwap"}, inplace=True)
    return ret


def obv(data):
    ret = data.ta.obv(append=True)
    data.rename(columns={"OBV": "obv"}, inplace=True)
    return ret


def bbands(data, length=10):
    return data.ta.bbands(length=length, append=True)
