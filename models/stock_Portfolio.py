import logging
from models.stock_position import stockPos

logger = logging.getLogger(__name__)

class stockPortfolio:
    def __init__(self):
        self.stocks = {}
    
    def addStock(self, stock):
        if not isinstance(stock, stockPos):
            raise TypeError("Only stockPos instances can be added to the portfolio.")
        if stock.ticker in self.stocks:
            existing_stock = self.stocks[stock.ticker]
            oldShares = existing_stock.shares
            existing_stock.shares += stock.shares
            existing_stock.boughtPrice = ((oldShares * existing_stock.boughtPrice) + (stock.shares * stock.boughtPrice)) / existing_stock.shares
            existing_stock.currPrice = stock.currPrice
            logger.info(f"Updated stock: {stock.ticker}, shares: {existing_stock.shares}, bought price: {existing_stock.boughtPrice}")
        else:
            self.stocks[stock.ticker] = stock
            logger.info(f"New stock added: {stock.ticker}, shares: {stock.shares}, bought price: {stock.boughtPrice}")

    def removePos(self, ticker):
        if ticker == "":
            raise ValueError("Ticker cannot be empty.")
        if ticker in self.stocks:
            del self.stocks[ticker]
        else:
            logger.error(f"Stock with ticker {ticker} not found in the portfolio.")
            raise ValueError("Stock with the given ticker not found in the portfolio.")
    
