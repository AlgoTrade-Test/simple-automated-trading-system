import pandas as pd
import yfinance as yf

def load_data(filepath):
    """
    Load stock data from a CSV file.
    """
    ticker = "AAPL"
    start="2021-01-01"
    end="2023-12-31"
    df = yf.download("AAPL", start=start, end=end)
    return df

def generate_signals(df):
    """
    Generate buy/sell signals using a simple moving average strategy.
    (To be implemented by the candidate)
    """
    # TODO: Calculate SMA (5) and SMA (20)
    # TODO: Generate buy/sell signals based on SMA crossover
    return df  # Return modified DataFrame with signals

def backtest_strategy(df, initial_balance=10000):
    """
    Simulate trading based on the generated signals.
    (To be implemented by the candidate)
    """
    # TODO: Implement trading logic (buy/sell decisions)
    # TODO: Track portfolio value over time
    return df  # Return modified DataFrame with portfolio values

def plot_results(df):
    """
    Plot stock price, moving averages, and buy/sell signals.
    Plotly is the recommended library
    (To be implemented by the candidate)
    """
    # TODO: Visualize stock price and signals
    pass

if __name__ == "__main__":
    # Load stock price data
    df = load_data("data/stock_data.csv")

    # Generate buy/sell signals
    df = generate_signals(df)

    # Run backtest
    df = backtest_strategy(df)

    # Plot results
    plot_results(df)
