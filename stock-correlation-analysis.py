import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class StockCorrelationAnalysis:
    def __init__(self, stock_files):
        self.function = "Comparing Stocks (Correlation Analysis)"
        self.stock_files = stock_files
        self.stocks_data = {}
        self.returns_df = pd.DataFrame()
        self.stock_files = stock_files
    
    def compute(self):
        for name, path in self.stock_files.items():
            df = pd.read_csv(path)
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.sort_values('Date')
            df['Daily Return'] = df['Adj Close'].pct_change()  # Calculate daily returns
            self.stocks_data[name] = df[['Date', 'Daily Return']].set_index('Date')

        self.returns_df = pd.concat(self.stocks_data.values(), axis=1)
        self.returns_df.columns = stock_files.keys()
        correlation_matrix = self.returns_df.corr()
        return correlation_matrix

    def visualize(self, correlation_matrix):
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title('Stock Correlation Matrix')
        plt.tight_layout()

        output_path = "./results/stock_correlation_analysis_results/correlation_heatmap.png"
        plt.savefig(output_path, dpi=300)  
        plt.close()  

my_symbols = ["AAPL", "NVDA", "AMD", "TSLA", "AMZN", "MSFT", "GOOGL"]

stock_files = {
    my_symbols[0]: "./stocks/"+my_symbols[0]+".csv",
    my_symbols[1]:"./stocks/"+my_symbols[1]+".csv",
    my_symbols[2]: "./stocks/"+my_symbols[2]+".csv",
    my_symbols[3]:"./stocks/"+my_symbols[3]+".csv",
    my_symbols[4]: "./stocks/"+my_symbols[4]+".csv",
    my_symbols[5]:"./stocks/"+my_symbols[5]+".csv",
    my_symbols[6]: "./stocks/"+my_symbols[6]+".csv"
} 


correlation_analysis_stocks = StockCorrelationAnalysis(stock_files)
correlation_matrix = correlation_analysis_stocks.compute()
correlation_analysis_stocks.visualize(correlation_matrix)

     
