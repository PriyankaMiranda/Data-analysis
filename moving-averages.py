import pandas as pd
import matplotlib.pyplot as plt
class MovingAverages:
    def __init__(self, file_path, symbol):
        self.function = "Moving Averages"
        self.file_path = file_path
        self.symbol = symbol
        self.stock_data = pd.DataFrame()

    def compute(self):
        self.stock_data = pd.read_csv(self.file_path)
        self.stock_data['Date'] = pd.to_datetime(self.stock_data['Date'])
        self.stock_data = self.stock_data.sort_values('Date')
        self.stock_data['Year_Month'] = self.stock_data['Date'].dt.strftime('%Y-%m')

        self.stock_data['MA_10'] = self.stock_data['Adj Close'].rolling(window=10).mean()  # 10-day moving average
        self.stock_data['MA_30'] = self.stock_data['Adj Close'].rolling(window=30).mean()  # 30-day moving average
    
    def visualize(self):
        plt.figure(figsize=(14, 7))
        plt.plot(self.stock_data['Year_Month'], self.stock_data['Adj Close'], label='Adjusted Close Price', color='blue')
        plt.plot(self.stock_data['Year_Month'], self.stock_data['MA_10'], label='10-Day Moving Average', color='green')
        plt.plot(self.stock_data['Year_Month'], self.stock_data['MA_30'], label='30-Day Moving Average', color='orange')
        plt.xticks(self.stock_data['Year_Month'][::251], rotation=45)  # 251 days in a stock market year 
        plt.xlabel('Year-Month')
        plt.ylabel('Price')
        plt.title('Stock Price with Moving Averages')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        output_path = "./results/moving_averages_results/"+self.symbol+".png"
        plt.savefig(output_path, dpi=300)  
        plt.close()  


my_symbols = ["AAPL", "NVDA", "AMD", "TSLA", "AMZN", "MSFT", "GOOGL"]

for symbol in my_symbols: 
    file_path = "./stocks/"+symbol+".csv" 
    moving_averges = MovingAverages(file_path, symbol)
    moving_averges.compute()
    moving_averges.visualize()
