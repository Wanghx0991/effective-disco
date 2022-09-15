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


