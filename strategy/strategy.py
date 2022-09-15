from datasource.akshare_source import Akshare
from .metrics import vwap,bbands
# from metrics import vwap,bbands
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


# if __name__ == "__main__":
symbol = "600036"
interval = "daily"
start_date, end_date = "20220715", "20220908"
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
data.loc[data["sig"] != "up", "up"] = float('nan')
data["down"] = data["high"] + 0.1
data.loc[data["sig"] != "down", "down"] = float('nan')


warmup = 10
sty = mpf.make_mpf_style(
        base_mpf_style="nightclouds", marketcolors=mpf.make_marketcolors(up="#ff8500", down="#1b90a7", inherit=True)
    )
kwargs = dict(
    type="candle",
    volume=True,
    style=sty,
    title=title,
    addplot=[
        mpf.make_addplot(data['vwap']),
        mpf.make_addplot(data[bbu_col]),
        mpf.make_addplot(data[bbl_col]),
        mpf.make_addplot(data['up'], type='scatter', marker='^', color='yellow', markersize=200),
        mpf.make_addplot(data['down'], type='scatter', marker='v', color='yellow', markersize=200),
    ],
)


fig, axes = mpf.plot(data, returnfig=True, **kwargs)
ax1 = axes[0]
ax2 = axes[2]
mpf.show()
