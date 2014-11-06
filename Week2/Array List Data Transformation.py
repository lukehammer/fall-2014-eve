__author__ = 'student'
test_data = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
]

master = {}
for x in test_data:
    ticker= x[1]
    list = master.keys()
    if ticker not in list:
        master[ticker] = []
    simple =[ x[0],x[2]]
    master[ticker].append(simple)


print master


















tickers = {}
for stock in test_data:
    symbol = stock[1]
    if not symbol in tickers.keys():
        tickers[symbol] = []
    items = tickers[symbol]
    items.append(stock)
