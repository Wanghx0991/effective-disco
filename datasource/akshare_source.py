import os
import pandas as pd
import akshare as ak
from datetime import datetime


class Akshare:
    # 单支股票的历史行情数据
    # 历史行情数据-东财
    # 目标地址: http: //quote.eastmoney.com / concept / sh603777.html?from=classic(示例)
    # 描述: 东方财富 - 沪深京A股日频率数据;历史数据按日频率更新, 当日收盘价请在收盘后获取
    # 限量: 单次返回指定沪深京A股上市公司、指定周期和指定日期间的历史行情日频率数据
    def stock_zh_a_hist(self, symbol, start_date, end_date, freq="daily", adjust=""):
        if freq not in ["daily", "weekly", "monthly"]:
            raise "please input the correct the frequency: {'daily', 'weekly', 'monthly'}"
        data = ak.stock_zh_a_hist(
            symbol=symbol, period=freq, start_date=start_date, end_date=end_date
        )
        data.columns = [
            "date",
            "open",
            "close",
            "high",
            "low",
            "volume",  # 成交量
            "amount",  # 成交额
            "amplitude",  # 涨幅
            "quote_change",  # 涨跌幅
            "ups_downs",  # 涨跌额
            "turnover",  # 换手率
        ]
        data["date"] = pd.DatetimeIndex(data["date"])
        data.index = data["date"]
        return data

    # 单只股票的分时图
    # 描述: 东方财富网-行情首页-沪深京 A 股-每日分时行情; 该接口只能获取近期的分时数据，注意时间周期的设置
    # 限量: 单次返回指定股票、频率、复权调整和时间区间的分时数据, 其中 1 分钟数据只返回近 5 个交易日数据且不复权
    def stock_zh_a_hist_min_em(
        self,
        symbol,
        start_date,
        end_date,
        freq="5",
    ):
        if freq not in ["1", "5", "15", "30", "60"]:
            raise "please input the correct the frequency: {'1', '5', '15', '30', '60'}"

        data = ak.stock_zh_a_hist_min_em(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            period="5",
            adjust="",
        )
        data.columns = [
            "date",
            "open",
            "close",
            "high",
            "low",
            "quote_change",  # 涨跌幅
            "ups_downs",  # 涨跌额
            "volume",  # 成交量
            "amount",  # 成交额
            "amplitude",  # 振幅
            "turnover",  # 换手率
        ]
        data["date"] = pd.DatetimeIndex(data["date"])
        data.index = data["date"]
        return data

    # 东方财富网-沪深京 A 股-实时行情数据
    # 限量: 单次返回所有沪深京 A 股上市公司的实时行情数据
    def stock_zh_a_spot_em(self):
        return ak.stock_zh_a_spot_em()
