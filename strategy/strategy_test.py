import unittest
from chart.charter import Charter

from datasource.akshare_source import Akshare
from operator import methodcaller


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.symbol = "600036"
        self.start_date = "20220815"
        self.end_date = "20220901"
        self.cli = Akshare()
        self.charter_cli = Charter(self.symbol, self.symbol)

    def test_something(self):
        data = self.cli.stock_zh_a_hist_min_em(
            self.symbol, start_date=self.start_date, end_date=self.end_date
        )
        # metric: vwap
        data.ta.vwap(append=True)

        # metric: 布林线 => length=10,表示bool的相关指标的前10列为Nan
        data.ta.bbands(length=10, append=True)
        bbu_col = [col for col in data.columns if "BBU" in col][0]
        bbl_col = [col for col in data.columns if "BBL" in col][0]
        pass


if __name__ == "__main__":
    unittest.main()
