import mplfinance as mpf
from DataSource import Akshare
import pandas as pd
import matplotlib.animation as animation


class Charter:
    def __init__(self, symbol, data, title, warm=10):
        self.price_ax1 = None
        self.volume_ax2 = None
        self.symbol = symbol
        self.warm = warm
        self.col = mpf.make_marketcolors(up="#ff8500", down="#1b90a7", inherit=True)
        self.sty = mpf.make_mpf_style(
            base_mpf_style="nightclouds", marketcolors=self.col
        )
        self.title = title
        data.index = pd.DatetimeIndex(data["date"])
        self.data = data

    def KChartPlotStatic(self):
        add = mpf.make_addplot(self.data["vwap"])
        # 默认指标及自定义指标, 如果需要添加自定义指标, 利用addplot参数
        kwargs = dict(
            type="candle",
            volume=True,
            style=self.sty,
            mav=(5, 10),
            addplot=add,
            title=self.title,
        )
        mpf.plot(data, **kwargs)

    def CustomMetric(self):
        # 如何加入自定义指标, 如 成交量加权(vwap)
        self.data["vwap"] = (
            ((self.data["high"] + self.data["low"]) / 2)
            * self.data["volume"].cumsum()
            / self.data["volume"].cumsum()
        )

    def KChartPlotDynamic(self, interval=1000):
        # 自定义指标需要同步配置
        _add = mpf.make_addplot(self.data.iloc[0 : self.warm]["vwap"])

        _kwargs = dict(
            type="candle",
            volume=True,
            style=self.sty,
            mav=(5, 10),
            addplot=_add,
            title=self.title,
        )

        fig, axes = mpf.plot(self.data.iloc[0 : self.warm], returnfig=True, **_kwargs)
        self.price_ax1 = axes[0]  # price
        self.volume_ax2 = axes[2]  # volume
        ani = animation.FuncAnimation(fig, self._animate, interval=interval)
        mpf.show()

    # animate 实时显示出图, 用来监控量化信号是否靠谱
    def _animate(self, i):
        # 动画原理: 每增加一次,从头画到我现在的位置,随后擦掉, 再画下一帧图
        _data = self.data.iloc[0 : (self.warm + i)]
        _add = mpf.make_addplot(_data["vwap"], ax=self.price_ax1)
        self.price_ax1.clear()
        self.volume_ax2.clear()
        _kwargs = dict(
            type="candle",
            style=self.sty,
            mav=(5, 10),
            addplot=_add,
        )
        mpf.plot(_data, ax=self.price_ax1, volume=self.volume_ax2, **_kwargs)


symbol = "600036"
interval = "daily"
start_date, end_date = "20220601", "20220908"
title = "%s_%s_%s" % (symbol, interval, start_date)

cli = Akshare()
data = cli.stock_zh_a_hist(symbol, start_date=start_date, end_date=end_date)

charter = Charter(symbol, data, title)
charter.CustomMetric()
charter.KChartPlotStatic()
charter.KChartPlotDynamic()
