from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import os

AV_API_KEY = os.environ["AV_API_KEY"]

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker

    def get_price(self):
        ts = TimeSeries(AV_API_KEY)
        return ts.get_daily(self.ticker)

    def get_recent_price(self):
        ts = TimeSeries(AV_API_KEY)
        return ts.get_intraday(self.ticker, interval="5min")

    def get_stochastic_oscillator(self):
        ti = TechIndicators(AV_API_KEY)
        return ti.get_stoch(self.ticker, "5min")