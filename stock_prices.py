import matplotlib.pyplot as plt
from pandas_datareader import data
from datetime import datetime

start_date = '03-01-2005'
end_date = datetime.now().strftime('%d-%m-%Y')

#ticker of deutsche bank stock from yahoo finance
stock = 'DB'


def get_data(ticker):
    try:
        stock_data = data.DataReader(ticker, 'yahoo', start_date, end_date)
        adj_close = clean_data(stock_data, 'Adj Close')
        create_plot(adj_close, ticker)
    except Exception:
        print(f'No data found for {ticker} stock')


def clean_data(stock_data, col):
    clean_data = stock_data[col]
    return clean_data


def create_plot(stock_data, ticker):
    stats = stock_data
    plt.grid(True)
    plt.plot(stats, linewidth=1, label=ticker)
    plt.title(f'{ticker} stock prices')
    plt.xlabel('Date')
    plt.ylabel('Price (€)')
    plt.legend()
    plt.show()


get_data(stock)