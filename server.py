from datasource.akshare_source import Akshare

if __name__ == '__main__':
    symbol = "600036"
    interval = "daily"
    start_date, end_date = "20220715", "20220908"
    title = "%s_%s_%s" % (symbol, interval, start_date)

    cli = Akshare()
    data = cli.stock_zh_a_hist(symbol, start_date=start_date, end_date=end_date)
    print(data)