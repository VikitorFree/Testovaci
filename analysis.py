import pandas as pd
import talib

def calculate_rsi(data, period=14):
    """
    Calculate the Relative Strength Index (RSI) for the given data.

    Parameters:
    data (pd.DataFrame): DataFrame containing 'close' prices.
    period (int): The period over which to calculate the RSI.

    Returns:
    pd.Series: A series of RSI values.
    """
    close_prices = data['close'].values
    rsi = talib.RSI(close_prices, timeperiod=period)
    return pd.Series(rsi, index=data.index)
