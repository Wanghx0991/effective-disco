import mplfinance as mpf
from DataSource import Akshare
import pandas as pd
import matplotlib.animation as animation

symbol = '600036'
interval = 'daily'
start_date = '20220601'
end_date = '20220908'

cli = Akshare()
data = cli.stock_zh_a_hist(symbol, start_date=start_date, end_date=end_date)
data.index = pd.DatetimeIndex(data['date'])

col = mpf.make_marketcolors(up='#ff8500', down='#1b90a7', inherit=True)
sty = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=col)

# 如何加入自定义指标, 如 成交量加权(vwap)
data['vwap'] = ((data['high'] + data['low']) / 2) * data['volume'].cumsum() / data['volume'].cumsum()
add = mpf.make_addplot(data['vwap'])

# 默认指标, 如果需要添加自定义指标, 利用addplot参数
kwargs = dict(type='candle', volume=True, style=sty, mav=(5, 10), addplot=add)

# mpf.plot(data,**kwargs)

#  动画实现(warmup先画20个,后续的再逐个实现
warmup = 20
_add = mpf.make_addplot(data.iloc[0:warmup]['vwap'])
_kwargs = dict(type='candle', volume=True, style=sty, mav=(5, 10), addplot=_add,
               title=symbol + ' ' + interval + '' + start_date)

fig, axes = mpf.plot(data.iloc[0:warmup], returnfig=True, **_kwargs)

ax1 = axes[0]  # price
ax2 = axes[2]  # volume


# animate 实时显示出图, 用来监控量化信号是否靠谱
def animate(i):
    # 动画原理: 每增加一次,从头画到我现在的位置,随后擦掉, 再画下一帧图
    _data = data.iloc[0:(warmup + i)]
    _add = mpf.make_addplot(_data['vwap'], ax=ax1)
    ax1.clear()
    ax2.clear()
    _kwargs = dict(type='candle', style=sty, mav=(5, 10), addplot=_add, )
    mpf.plot(_data, ax=ax1, volume=ax2, **_kwargs)


ani = animation.FuncAnimation(fig, animate, interval=100)
mpf.show()
pass


#
