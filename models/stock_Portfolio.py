from models.stock_position import stockPos


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
            print(f"Stock with ticker {stock.ticker} updated in the portfolio.")
        else:
            self.stocks[stock.ticker] = stock
            print(f"Stock with ticker {stock.ticker} added to the portfolio.")
            
    def removePos(self, ticker):
        if ticker == "":
            raise ValueError("Ticker cannot be empty.")
        if ticker in self.stocks:
            del self.stocks[ticker]
        else:
            raise ValueError("Stock with the given ticker not found in the portfolio.")
    
    def viewPortfolio(self):
        if not self.stocks:
            print("Portfolio is empty.")
            return
        for stock in self.stocks.values():
            print(f"Ticker: {stock.ticker}, Shares: {stock.shares}, Bought price: {stock.boughtPrice}, Current price: {stock.currPrice}")

