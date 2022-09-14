import unittest
import pandas_ta as ta
from chart.charter import Charter
from datasource.akshare_source import Akshare
from strategy.metrics import obv
from strategy.metrics import vwap


class MyTestCase(unittest.TestCase):
    def setUp(self):
        symbol = "600036"
        interval = "daily"
        start_date, end_date = "20220601", "20220908"
        title = "%s_%s_%s" % (symbol, interval, start_date)
        self.cli = Charter(sym=symbol, tit=title)
        self.cli_datasource = Akshare()
        self.data = self.cli_datasource.stock_zh_a_hist(
            symbol, start_date=start_date, end_date=end_date
        )

    def test_KChartPlotStatic(self):
        self.cli.KChartPlotStatic(self.data, metrics={"obv": "y", "vwap": "r"})
        pass


if __name__ == "__main__":
    unittest.main()
