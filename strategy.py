import akshare as ak


class Strategy:
    def __init__(self, start_date, end_date, ma, code):
        self.stock_zh_a_hist_df = ak.stock_zh_a_hist(
            symbol=code,
            period="daily",
            start_date=start_date,
            end_date=end_date,
            adjust="",
        )

    def execute(self):
        # buy: price < ma20 * 0.95
        # sell: price > ma29 * 1.05
        pass


strategy = Strategy(start_date="20200101", end_date="20200906", ma=10, code="603777")
