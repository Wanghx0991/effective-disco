import unittest

from datasource.akshare_source import Akshare


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.symbol = "600036"
        self.start_date = "20220901"
        self.end_date = "20220901"
        self.cli = Akshare()

    def test_stock_zh_a_hist_min_em(self):
        data = self.cli.stock_zh_a_hist_min_em(
            self.symbol, start_date=self.start_date, end_date=self.end_date
        )
        self.assertIsNotNone(data)

    def test_stock_zh_a_hist(self):
        data = self.cli.stock_zh_a_hist(
            self.symbol, start_date=self.start_date, end_date=self.end_date
        )
        self.assertIsNotNone(data)


if __name__ == "__main__":
    unittest.main()
