import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class VolatilityAnalysis:
    def __init__(self, stock_files, symbol):
        self.function = "Determines Volatility of a Stock"
        self.stock_files = stock_files
        self.symbol = symbol
        self.stocks_data = {}

    def compute(self):
        for name, path in self.stock_files.items():
            df = pd.read_csv(path)
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.sort_values('Date')
            df['Daily Return'] = df['Adj Close'].pct_change()  # Calculate daily returns
            self.stocks_data[name] = df[['Date', 'Daily Return']].set_index('Date')

        self.returns_df = pd.concat(self.stocks_data.values(), axis=1)
        self.returns_df.columns = self.stock_files.keys()

        daily_volatility = self.returns_df.std()
        rolling_window = 30
        rolling_volatility = self.returns_df.rolling(window=rolling_window).std()
        return rolling_volatility

    def visualize(self, rolling_volatility):
        rolling_window = 30
        plt.figure(figsize=(12, 6))
        for stock in rolling_volatility.columns:
            plt.plot(rolling_volatility.index, rolling_volatility[stock], label=f'{stock} (Rolling Volatility)')

        plt.title(f'{rolling_window}-Day Rolling Volatility of Stocks')
        plt.xlabel('Date')
        plt.ylabel('Volatility (Standard Deviation)')
        plt.legend()
        plt.grid()

        output_path = "./results/volatility_results/"+self.symbol+".png"
        plt.savefig(output_path, dpi=300)  
        plt.close()  

my_symbols = ["AAPL", "NVDA", "AMD", "TSLA", "AMZN", "MSFT", "GOOGL"]
full_file_paths = {}

for symbol in my_symbols: 
    file_path = "./stocks/"+symbol+".csv"
    full_file_paths[symbol] = file_path

volatiltiy_analysis = VolatilityAnalysis(full_file_paths, symbol)
rolling_volatility = volatiltiy_analysis.compute()
volatiltiy_analysis.visualize(rolling_volatility)