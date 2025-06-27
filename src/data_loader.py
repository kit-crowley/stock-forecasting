import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, period: str = "5y", interval: str = "1d") -> pd.DataFrame:
    """
    Fetch historical stock data from Yahoo Finance.

    Args:
        ticker (str): Stock ticker symbol, e.g. 'AAPL'
        period (str): Data period to download (e.g. '1mo', '1y', '5y', 'max')
        interval (str): Data interval (e.g. '1d', '1h', '1wk')

    Returns:
        pd.DataFrame: DataFrame with Date as index and OHLCV columns
    """
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)

    if df.empty:
        raise ValueError(f"No data found for ticker '{ticker}' with period '{period}' and interval '{interval}'")

    # Make sure the index is datetime type
    df.index = pd.to_datetime(df.index)
    return df

if __name__ == "__main__":
    # Quick test run
    ticker = "AAPL"
    print(f"Fetching data for {ticker}...")
    data = fetch_stock_data(ticker)
    print(data.head())
