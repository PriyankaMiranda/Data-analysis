import pandas as pd
import matplotlib.pyplot as plt
class ComparingStocks:
    def __init__(self, stock_files, symbol1, symbol2):
        self.function = "Comparing Stocks"
        self.stock_files = stock_files
        self.symbol1 = symbol1
        self.symbol2 = symbol2
        self.stocks_data = {}
    
    def compute(self):
        for name, path in self.stock_files.items():
            df = pd.read_csv(path)
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.sort_values('Date')
            df['Normalized Price'] = df['Adj Close'] / df['Adj Close'].iloc[0] * 100
            self.stocks_data[name] = df

    def visualize(self):
        plt.figure(figsize=(14, 7))
        for name, df in self.stocks_data.items():
            plt.plot(df['Date'], df['Normalized Price'], label=name)

        plt.xlabel('Date')
        plt.ylabel('Normalized Price')
        plt.title('Comparison of Stock Prices')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        output_path = "./results/stock_comparison_results/"+self.symbol1+"_"+self.symbol2+".png"
        plt.savefig(output_path, dpi=300)  
        plt.close()  

my_symbols = ["AAPL", "NVDA", "AMD", "TSLA", "AMZN", "MSFT", "GOOGL"]

for loc in range(0, len(my_symbols)):
    for loc2 in range(loc+1, len(my_symbols)):
        symbol1 = my_symbols[loc]
        symbol2 = my_symbols[loc2]
        stock_files = {
            symbol1: "./stocks/"+symbol1+".csv",
            symbol2:"./stocks/"+symbol2+".csv"
            } 
        comparing_stocks = ComparingStocks(stock_files, symbol1, symbol2)
        comparing_stocks.compute()
        comparing_stocks.visualize()

     
