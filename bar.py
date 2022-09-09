# from DataSource import GetAkHistoryData


class Bar:
    def __init__(self, frequency="d"):
        self.eob = None  # bar结束时间
        self.bob = None  # bar开始时间
        self.volume = None  # int
        self.amount = None  # float
        self.low = None  # float
        self.high = None  # float
        self.closed = None  # float
        self.started = None  # float
        self.frequency = frequency

    def buildBar(self, high_arr, low_arr, started_arr, closed_arr):
        self.high = high_arr.max()
        self.low = low_arr.min()
        self.started = started_arr[0][0]
        self.closed = closed_arr[-1][-1]


if __name__ == "__main__":
    pass
    # summary = GetAkHistoryData(symbol='603777', start_date='20200701', end_date='20200906')
    #
    # splitBy = 5
    # discarded = int(len(summary)) % splitBy
    # rows = int(len(summary) / splitBy)
    #
    # high_arr = summary['最高'][discarded:].to_numpy().reshape(rows,splitBy)
    # low_arr = summary['最低'][discarded:].to_numpy().reshape(rows,splitBy)
    # started_arr = summary['开盘'][discarded:].to_numpy().reshape(rows,splitBy)
    # closed_arr = summary['收盘'][discarded:].to_numpy().reshape(rows,splitBy)
    #
    # bars = {}
    # for i in range(rows):
    #     obj = Bar()
    #     obj.buildBar(high_arr,low_arr,started_arr,closed_arr)
    #     bars[i] = obj
