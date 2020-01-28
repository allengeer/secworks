import unittest
from secworks.model import Stock

class MyTestCase(unittest.TestCase):
    def test_stock_object(self):
        stock = Stock("GOOG")
        self.assertEquals("GOOG", stock.ticker)

    def test_stock_price(self):
        stock = Stock("GOOG")
        price_frame = stock.get_price()
        print (len(price_frame))

    def test_stoch_indicator(self):
        stock = Stock("GOOG")
        stoch_indicators = stock.get_stochastic_oscillator()
        print(stoch_indicators)

    def test_intra_price(self):
        stock = Stock("PD")
        intra_price = stock.get_recent_price()
        print(intra_price)

if __name__ == '__main__':
    unittest.main()
