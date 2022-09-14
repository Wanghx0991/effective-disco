from datasource.akshare_source import Akshare
from metrics import vwap, bbands
import mplfinance as mpf
import matplotlib.animation as animation


class Filter:
    def __init__(self):
        self.sig = None

    def update(self, bars):
        #  示例 只用最后一个,根据实际情况
        data = bars.iloc[-1]
        if data["close"] > data[bbu_col]:
            self.sig = "down"
        elif data["close"] < data[bbl_col]:
            self.sig = "up"
        else:
            self.sig = None


if __name__ == "__main__":
    symbol = "600036"
    interval = "daily"
    start_date, end_date = "20220415", "20220908"
    title = "%s_%s_%s" % (symbol, interval, start_date)

    cli = Akshare()
    data = cli.stock_zh_a_hist(symbol, start_date=start_date, end_date=end_date)

    vwap(data)
    bbands(data)

    bbu_col = [col for col in data.columns if "BBU" in col][0]
    bbl_col = [col for col in data.columns if "BBL" in col][0]

    f = Filter()
    sig = []
    for i in range(data.shape[0]):
        f.update(data.iloc[: (i + 1)])
        sig.append(f.sig)

    data["sig"] = sig

    data["up"] = data["low"] - 0.1
    data.loc[data["sig"] != "up", "up"] = float("nan")
    data["down"] = data["high"] - 0.1
    data.loc[data["sig"] != "down", "down"] = float("nan")
    pass

    # warmup = 10
    # kwargs = dict(
    #     type="candle",
    #     volume=True,
    #     style=mpf.make_mpf_style(
    #         base_mpf_style="nightclouds", marketcolors=mpf.make_marketcolors(up="#ff8500", down="#1b90a7", inherit=True)
    #     ),
    #     title=title,
    # )
    # fig, axes = mpf.plot(data.iloc[0:warmup], returnfig=True, **kwargs)
    # ax1, ax2 = axes[0], axes[2]
    #
    #
    # def _animate(ival):
    #     _data = data.iloc[0:(warmup + ival)]
    #     _kwargs = dict(
    #         type="candle",
    #         style=mpf.make_mpf_style(
    #             base_mpf_style="nightclouds",
    #             marketcolors=mpf.make_marketcolors(up="#ff8500", down="#1b90a7", inherit=True)
    #         ),
    #         # mav=(5, 10),
    #         addplot=[
    #             mpf.make_addplot(_data['vwap'], ax=ax1),
    #             mpf.make_addplot(_data[bbu_col], ax=ax1),
    #             mpf.make_addplot(_data[bbl_col], ax=ax1),
    #             mpf.make_addplot(_data['up'],type='scatter',marker='^',color='yellow',markersize=200, ax=ax1),
    #             mpf.make_addplot(_data['down'], type='scatter', marker='v', color='yellow', markersize=200, ax=ax1),
    #         ],
    #     )
    #     ax1.clear()
    #     ax2.clear()
    #     mpf.plot(_data, ax=ax1, volume=ax2, **_kwargs)
    #
    #
    # animation.FuncAnimation(
    #     fig,
    #     _animate,
    #     interval=100,
    # )
    # mpf.show()
