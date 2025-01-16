import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class BetaCalc:
    def __init__(self, stock_files, symbol):
        self.function = "Determines sensitvity of a stock"
        self.stock_files = stock_files
        self.symbol = symbol
        self.stocks_data = {}

    def compute(self, benchmark_returns):
        returns_df = pd.DataFrame()
        aligned_data = returns_df.join(benchmark_returns, how='inner', rsuffix='_benchmark')

        beta_values = {}
        for stock in returns_df.columns:
            # Calculate covariance and variance
            covariance = aligned_data[stock].cov(aligned_data['Daily Return_benchmark'])
            variance = aligned_data['Daily Return_benchmark'].var()
            beta = covariance / variance
            beta_values[stock] = beta

        beta_df = pd.DataFrame(list(beta_values.items()), columns=['Stock', 'Beta'])
        return beta_df

    def visualize(self, beta_df):
        plt.figure(figsize=(12, 6))
        plt.bar(beta_df['Stock'], beta_df['Beta'], color='skyblue', edgecolor='black')
        plt.axhline(1, color='red', linestyle='--', label='Market Beta (1)')
        plt.axhline(0, color='green', linestyle='--', label='Neutral Beta (0)')
        plt.title('Beta Values of Stocks Relative to the Market')
        plt.xlabel('Stocks')
        plt.ylabel('Beta Value')
        plt.xticks(rotation=45, ha='right')
        plt.legend()
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        output_path = "./results/sensitivity_results/"+self.symbol+".png"
        plt.savefig(output_path, dpi=300)  
        plt.close()  

benchmark_path = "./etfs/SPY.csv"
benchmark_data = pd.read_csv(benchmark_path)
benchmark_data['Date'] = pd.to_datetime(benchmark_data['Date'])
benchmark_data = benchmark_data.sort_values('Date')
benchmark_data['Daily Return'] = benchmark_data['Adj Close'].pct_change()
benchmark_returns = benchmark_data[['Date', 'Daily Return']].set_index('Date')

my_symbols = ["AAPL", "NVDA", "AMD", "TSLA", "AMZN", "MSFT", "GOOGL"]
full_file_paths = {}
for symbol in my_symbols: 
    file_path = "./stocks/"+symbol+".csv"
    full_file_paths[symbol] = file_path

sensitivity_analysis = BetaCalc(full_file_paths, symbol)
sensitivity = sensitivity_analysis.compute(benchmark_returns)
sensitivity_analysis.visualize(sensitivity)