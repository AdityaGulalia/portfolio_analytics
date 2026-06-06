import pytest
from models.stock_position import stockPos
from models.stock_Portfolio import stockPortfolio

@pytest.mark.parametrize("ticker, shares, bought_price, curr_price", [
    (1, 10, 150.0, 155.0),
    ("GOOGL", 5, 2000.0, 2050.0),
    ("MSFT", 20, 250.0, 260.0)
])
def test_stock_position_creation(ticker, shares, bought_price, curr_price):
    stock = stockPos(ticker, shares, bought_price, curr_price)
    assert stock.ticker == ticker
    assert stock.shares == shares
    assert stock.boughtPrice == bought_price
    assert stock.currPrice == curr_price
    
    
    