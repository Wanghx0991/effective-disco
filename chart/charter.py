import pandas as pd
import pandas_ta as ta
import mplfinance as mpf
import matplotlib.animation as animation
from datasource.akshare_source import Akshare
from strategy.metrics import obv, vwap


class Charter:
    def __init__(self, sym, tit, warm=10):
        self.symbol = sym
        self.warm = warm
        self.col = mpf.make_marketcolors(up="#ff8500", down="#1b90a7", inherit=True)
        self.sty = mpf.make_mpf_style(
            base_mpf_style="nightclouds", marketcolors=self.col
        )
        self.title = tit
        self.data = None
        self.price_ax1 = None
        self.volume_ax2 = None

    def _addConfig(self, candle_data, data_range="all", **kwarg):
        add_plot = []
        if data_range == "all":
            for value, color in kwarg["metrics"].items():
                if value == "obv":
                    add_plot.append(mpf.make_addplot(obv(candle_data), color=color))
                elif value == "vwap":
                    add_plot.append(mpf.make_addplot(vwap(candle_data), color=color))
        elif type(data_range) == int:
            for value, color in kwarg["metrics"].items():
                if value == "obv":
                    add_plot.append(
                        mpf.make_addplot(obv(candle_data)[0 : self.warm], color=color)
                    )
                elif value == "vwap":
                    add_plot.append(
                        mpf.make_addplot(vwap(candle_data)[0 : self.warm], color=color)
                    )

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

    def KChartPlotStatic(self, candle_data, data_range="all", **kwarg):
        kwargs = self._addConfig(candle_data, data_range, **kwarg)
        mpf.plot(candle_data, **kwargs)

    def KChartPlotDynamic(self, candle_data, inter=100, **kwargs):
        param = self._addConfig(candle_data, data_range=self.warm, **kwargs)
        fig, axes = mpf.plot(candle_data.iloc[0 : self.warm], returnfig=True, **param)
        self.price_ax1 = axes[0]  # price
        self.volume_ax2 = axes[2]  # volume

        # animate 实时显示出图, 用来监控量化信号是否靠谱
        def _animate(ival):
            # 动画原理: 每增加一次,从头画到我现在的位置,随后擦掉, 再画下一帧图
            _data = candle_data.iloc[0 : (self.warm + ival)]
            add_plot = []
            for value, color in kwargs["metrics"].items():
                if value == "obv":
                    add_plot.append(
                        mpf.make_addplot(_data["obv"], color=color, ax=self.volume_ax2)
                    )
                elif value == "vwap":
                    add_plot.append(
                        mpf.make_addplot(_data["vwap"], color=color, ax=self.price_ax1)
                    )
            self.price_ax1.clear()
            self.volume_ax2.clear()
            _kwargs = dict(
                type="candle",
                style=self.sty,
                mav=(5, 10),
                addplot=add_plot,
            )
            mpf.plot(_data, ax=self.price_ax1, volume=self.volume_ax2, **_kwargs)

        animation.FuncAnimation(
            fig,
            _animate,
            interval=inter,
        )
        mpf.show()


if __name__ == "__main__":
    pass
    # symbol = "600036"
    # interval = "daily"
    # start_date, end_date = "20220815", "20220908"
    # title = "%s_%s_%s" % (symbol, interval, start_date)
    #
    # cli = Akshare()
    # data = cli.stock_zh_a_hist(symbol, start_date=start_date, end_date=end_date)
    #
    # charter = Charter(symbol, title)
    # charter.KChartPlotStatic(data, metrics={"obv": "y", "vwap": "r"})
    # charter.KChartPlotDynamic(data, metrics={"vwap": "r"})
