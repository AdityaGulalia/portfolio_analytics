from altair import value
from numpy import save

from models.stock_position import stockPos
from models.stock_Portfolio import stockPortfolio
from storage.json_storage import JSONStorage
from analytics.portfolio_analytics import PortfolioAnalytics
def main():
    portfolio = stockPortfolio()
    
    try:
        stock1 = stockPos("AAPL", 10, 100.0, 170.0)
        stock2 = stockPos("NVDA", 5, 200.0, 2800.0)
        
        # stock1_dict = stock1.to_dict()
        # stock2_dict = stock2.to_dict()
        
        
        # print(stockPos.from_dict(stock1_dict))
        # print(stockPos.from_dict(stock2_dict))
        
        # print(stock1.ticker)
        # print(stock1.shares)
        # print(stock1.boughtPrice)
        # print(stock1.currPrice)
        portfolio.addStock(stock1)
        
        portfolio.addStock(stock2)
        cost = PortfolioAnalytics.calculateTotalCost(portfolio)
        value = PortfolioAnalytics.calculateTotalValue(portfolio)
        pnl = PortfolioAnalytics.calculatePNL(portfolio)

        print(cost)
        print(value)
        print(pnl)
        print(value - cost)
        # JSONStorage.save(portfolio, "/Users/adityagulalia/Desktop/py/track_it/reports/portfolio.json")
        
    except ValueError as ve:
        print(f"Value error: {ve}")
    except TypeError as te:
        print(f"Type error: {te}")

if __name__ == "__main__":
    main()