import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
class StockVolatility:
    def __init__(self, file_path, symbol):
        self.function = "Determines Stock Volatility"
        self.file_path = file_path
        self.symbol = symbol
        self.stock_data = pd.DataFrame()

    def compute(self):
        self.stock_data = pd.read_csv(self.file_path)
        self.stock_data['Date'] = pd.to_datetime(self.stock_data['Date'])
        self.stock_data['Year_Month'] = self.stock_data['Date'].dt.strftime('%Y-%m')
        # Check adjusted closing price for each date 
        # Get percentage change by compring the current and the next data
        self.stock_data['Daily Return'] = self.stock_data['Adj Close'].pct_change()
        # Check standard deviation of the change over a 1 month window (volatility) 
        self.stock_data['Volatility (Monthly)'] = self.stock_data['Daily Return'].rolling(window=30).std()
        # Check standard deviation of the change over a 6 months window (volatility) 
        self.stock_data['Volatility (Bi-annual)'] = self.stock_data['Daily Return'].rolling(window=(30*3)+(31*3)).std()
        # Check standard deviation of the change over a 1 year window (volatility) 
        self.stock_data['Volatility (Yearly)'] = self.stock_data['Daily Return'].rolling(window=365).std()
        
    def visualize(self):
        plt.figure(figsize=(14, 7))
        plt.plot(self.stock_data['Year_Month'], self.stock_data['Volatility (Monthly)'], label='Volatility (1 month)', color='blue')
        plt.plot(self.stock_data['Year_Month'], self.stock_data['Volatility (Bi-annual)'], label='Volatility (6 months)', color='orange')
        plt.plot(self.stock_data['Year_Month'], self.stock_data['Volatility (Yearly)'], label='Volatility (12 months)', color='red')

        plt.xticks(self.stock_data['Year_Month'][::251], rotation=45)  # 251 days in a stock market year 
        plt.xlabel('Year-Month')
        plt.ylabel('Volatility')
        plt.title('Stock Price and Volatility')
        plt.legend()
        plt.tight_layout()
        
        output_path = "./results/stock_volatility_results/"+self.symbol+".png"
        plt.savefig(output_path, dpi=300)  
        plt.close()  

my_symbols = ["AAPL", "NVDA", "AMD", "TSLA", "AMZN", "MSFT", "GOOGL"]

for symbol in my_symbols: 
    file_path = "./stocks/"+symbol+".csv" 
    volatility_predictor = StockVolatility(file_path, symbol)
    volatility_predictor.compute()
    volatility_predictor.visualize()