import pytest
import unittest
import yfinance as yf
from unittest.mock import patch, Mock 
from models.stock_position import stockPos
from models.stock_Portfolio import stockPortfolio
from data.market_data import MarketData

# @pytest.mark.parametrize("ticker, shares, bought_price, curr_price", [
#     (1, 10, 150.0, 155.0),
#     ("GOOGL", 5, 2000.0, 2050.0),
#     ("MSFT", 20, 250.0, 260.0)
# ])
# def test_stock_position_creation(ticker, shares, bought_price, curr_price):
#     stock = stockPos(ticker, shares, bought_price, curr_price)
#     assert stock.ticker == ticker
#     assert stock.shares == shares
#     assert stock.boughtPrice == bought_price
#     assert stock.currPrice == curr_price
    
class test_market_data(unittest.TestCase):
    
    @patch('data.market_data.yf.Tickers')
    def test_get_stock_prices(self, mock_tickers):
        
        stock_ticker = Mock()
        stock_ticker.fast_info = {"lastPrice": 150.0}
        mock_ticker = Mock()
        mock_ticker.tickers = {"AAPL": stock_ticker}
        
        mock_tickers.return_value = mock_ticker
        
        result = MarketData.fetch_stock_prices("AAPL")
        self.assertEqual(result, {"AAPL": 150.0})