import unittest

from datasource.akshare_source import Akshare
from metrics import obv
from metrics import vwap
from metrics import bbands


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.symbol = "600036"
        self.start_date = "20220815"
        self.end_date = "20220901"
        self.cli_datasource = Akshare()
        self.data = self.cli_datasource.stock_zh_a_hist(self.symbol, start_date=self.start_date, end_date=self.end_date)

    def test_obv(self):
        obv(self.data)
        self.assertIsNotNone(self.data["obv"])

    def test_vwap(self):
        vwap(self.data)
        self.assertIsNotNone(self.data["vwap"])

    def test_bbands(self):
        bbands(self.data)
        self.assertIsNotNone(self.data["BBL_10_2.0"])
        self.assertIsNotNone(self.data["BBM_10_2.0"])
        self.assertIsNotNone(self.data["BBU_10_2.0"])
        self.assertIsNotNone(self.data["BBB_10_2.0"])
        self.assertIsNotNone(self.data["BBP_10_2.0"])


if __name__ == "__main__":
    unittest.main()
