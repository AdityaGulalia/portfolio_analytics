from models.stock_Portfolio import stockPortfolio
from models.stock_position import stockPos

class PortfolioAnalytics:
    
    @staticmethod
    def _validate_portfolio(portfolio):
        if not isinstance(portfolio, stockPortfolio):
            raise TypeError("Only stockPortfolio instances can be analyzed")
    
    @staticmethod
    def calculateTotalValue(portfolio):
        PortfolioAnalytics._validate_portfolio(portfolio)
        total_value = 0.0
        for stock in portfolio.stocks.values():
            total_value += stock.market_value()
        
        return total_value
    
    @staticmethod
    def calculateTotalCost(portfolio):
        PortfolioAnalytics._validate_portfolio(portfolio)
        total_cost = 0.0
        for stock in portfolio.stocks.values():
            total_cost += stock.cost_basis()
            
        return total_cost
    
    @staticmethod
    def calculatePNL(portfolio):
        PortfolioAnalytics._validate_portfolio(portfolio)
        pnl = 0.0
        for stock in portfolio.stocks.values():
            pnl += stock.pnl()
            
        return pnl
    
    @staticmethod
    def best_performing_stock(portfolio):
        PortfolioAnalytics._validate_portfolio(portfolio)
        best_stock = None
        best_pnl = float('-inf')
        
        for stock in portfolio.stocks.values():
            stock_pnl = stock.pnl()
            if stock_pnl > best_pnl:
                best_pnl = stock_pnl
                best_stock = stock
        
        return best_stock
    
    @staticmethod
    def worst_performing_stock(portfolio):
        PortfolioAnalytics._validate_portfolio(portfolio)
        worst_stock = None
        worst_pnl = float('inf')
        
        for stock in portfolio.stocks.values():
            stock_pnl = stock.pnl()
            if stock_pnl < worst_pnl:
                worst_pnl = stock_pnl
                worst_stock = stock
        
        return worst_stock
    
    @staticmethod
    def portfolio_summary(portfolio):
        PortfolioAnalytics._validate_portfolio(portfolio)
        summary = {
            "total_value": PortfolioAnalytics.calculateTotalValue(portfolio),
            "total_cost": PortfolioAnalytics.calculateTotalCost(portfolio),
            "total_pnl": PortfolioAnalytics.calculatePNL(portfolio),
            "best_stock": PortfolioAnalytics.best_performing_stock(portfolio),
            "worst_stock": PortfolioAnalytics.worst_performing_stock(portfolio)
        }
        return summary