import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class ReturnsAnalysis:
    def __init__(self, file_path, symbol):
        self.function = "Determines Stock Returns"
        self.file_path = file_path
        self.symbol = symbol
        self.stock_data = pd.DataFrame()

    def compute(self):
        self.stock_data = pd.read_csv(self.file_path)
        self.stock_data['Date'] = pd.to_datetime(self.stock_data['Date'])
        self.stock_data = self.stock_data.sort_values('Date')
        self.stock_data['Daily Return'] = self.stock_data['Adj Close'].pct_change()
        self.stock_data['Cumulative Return'] = (1 + self.stock_data['Daily Return']).cumprod() - 1
        
    def visualize(self):
        plt.figure(figsize=(14, 7))
        plt.subplot(2, 1, 1)  
        plt.plot(self.stock_data['Date'], self.stock_data['Daily Return'], label='Daily Return', color='blue')
        plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
        plt.title('Daily Returns')
        plt.ylabel('Daily Return')
        plt.xticks(rotation=45)

        plt.subplot(2, 1, 2) 
        plt.plot(self.stock_data['Date'], self.stock_data['Cumulative Return'], label='Cumulative Return', color='green')
        plt.title('Cumulative Returns')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Return')
        plt.xticks(rotation=45)

        plt.tight_layout()

        output_path = "./results/returns_analysis_results/"+self.symbol+".png"
        plt.savefig(output_path, dpi=300)  
        plt.close()  

my_symbols = ["AAPL", "NVDA", "AMD", "TSLA", "AMZN", "MSFT", "GOOGL"]

for symbol in my_symbols: 
    file_path = "./stocks/"+symbol+".csv" 
    returns_analysis = ReturnsAnalysis(file_path, symbol)
    returns_analysis.compute()
    returns_analysis.visualize()