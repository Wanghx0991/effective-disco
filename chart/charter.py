import pandas as pd
import pandas_ta as ta
import mplfinance as mpf
import matplotlib.animation as animation
from datasource.akshare_source import Akshare
from strategy.metrics import obv, vwap


class Charter:
    def __init__(self, symbol, title, warm=10):
        self.symbol = symbol
        self.warm = warm
        self.col = mpf.make_marketcolors(up="#ff8500", down="#1b90a7", inherit=True)
        self.sty = mpf.make_mpf_style(
            base_mpf_style="nightclouds", marketcolors=self.col
        )
        self.title = title
        self.price_ax1 = None
        self.volume_ax2 = None

    def KChartPlotStatic(self, data, **kwarg):
        kwargs = self._addConfig(**kwarg)
        mpf.plot(data, **kwargs)

    def KChartPlotDynamic(self, data, interval=10, **kwarg):
        add_plot = []
        for value, color in kwarg["metrics"].items():
            if value == "obv":
                add_plot.append(mpf.make_addplot(obv(data)[0:self.warm], color=color))
            elif value == "vwap":
                add_plot.append(mpf.make_addplot(vwap(data)[0:self.warm], color=color))

        _kwargs = dict(
            type="candle",
            volume=True,
            style=self.sty,
            mav=(5, 10),
            title=self.title,
        )
        if len(add_plot) != 0:
            _kwargs["addplot"] = add_plot

        fig, axes = mpf.plot(data.iloc[0: self.warm], returnfig=True, **_kwargs)
        self.price_ax1 = axes[0]  # price
        self.volume_ax2 = axes[2]  # volume
        animation.FuncAnimation(
            fig,
            self._animate,
            interval=interval,
        )
        mpf.show()

    def _addConfig(self, **kwarg):
        add_plot = []
        for value, color in kwarg["metrics"].items():
            if value == "obv":
                add_plot.append(mpf.make_addplot(obv(data), color=color))
            elif value == "vwap":
                add_plot.append(mpf.make_addplot(vwap(data), color=color))

        _kwargs = dict(
            type="candle",
            volume=True,
            style=self.sty,
            mav=(5, 10),
            title=self.title,
        )
        if len(add_plot) != 0:
            _kwargs["addplot"] = add_plot
        return _kwargs

    # animate 实时显示出图, 用来监控量化信号是否靠谱
    def _animate(self, ival,data):
        # 动画原理: 每增加一次,从头画到我现在的位置,随后擦掉, 再画下一帧图
        _data = data.iloc[0: (self.warm + ival)]
        _add = [
            mpf.make_addplot(_data["vwap"], ax=self.price_ax1, color='y'),
            mpf.make_addplot(_data["obv"], ax=self.price_ax1, color='r'),
        ]
        self.price_ax1.clear()
        self.volume_ax2.clear()
        _kwargs = dict(
            type="candle",
            style=self.sty,
            mav=(5, 10),
            addplot=_add,
        )
        mpf.plot(_data, ax=self.price_ax1, volume=self.volume_ax2, **_kwargs)


if __name__ == "__main__":
    symbol = "600036"
    interval = "daily"
    start_date, end_date = "20220501", "20220908"
    title = "%s_%s_%s" % (symbol, interval, start_date)

    cli = Akshare()
    data = cli.stock_zh_a_hist(symbol, start_date=start_date, end_date=end_date)
    charter = Charter(symbol, title)
    # charter.KChartPlotStatic(data, metrics={"obv": "y", "vwap": "r"})
    charter.KChartPlotDynamic(data, metrics={"obv": "y", "vwap": "r"})
