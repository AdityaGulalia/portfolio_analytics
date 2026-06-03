from models.stock_Portfolio import stockPortfolio
from models.stock_position import stockPos
import json

class JSONStorage:
    
    @staticmethod
    def save(portfolio, filename):
        if not isinstance(portfolio, stockPortfolio):
            raise TypeError("Only stockPortfolio instances can be saved")
        
        data = []
        for stock in portfolio.stocks.values():
            data.append(stock.to_dict())
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    @staticmethod       
    def load(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            portfolio = stockPortfolio()
            for stocks in data:
                stocks_obj = stockPos.from_dict(stocks)
                portfolio.addStock(stocks_obj)
                return portfolio
                