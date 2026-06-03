from models.stock_position import stockPos
from models.stock_Portfolio import stockPortfolio
from storage.json_storage import JSONStorage
from analytics.portfolio_analytics import PortfolioAnalytics
from data.market_data import MarketData

def main():
    portfolio = stockPortfolio()
    
    try:
        portfolio = JSONStorage.load("/Users/adityagulalia/Desktop/py/track_it/reports/portfolio.json")
        print(portfolio.viewPortfolio())
        
        updated_portfolio = MarketData.update_portfolio_prices(portfolio)
        print(updated_portfolio.viewPortfolio())
        
        
    except ValueError as ve:
        print(f"Value error: {ve}")
    except TypeError as te:
        print(f"Type error: {te}")

if __name__ == "__main__":
    main()