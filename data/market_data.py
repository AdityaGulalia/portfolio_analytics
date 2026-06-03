import yfinance as yf

from models.stock_Portfolio import stockPortfolio

class MarketData:
    
    @staticmethod
    def fetch_stock_prices(tickers):
        try:
            tickers_obj = yf.Tickers(tickers)
            last_price = {}
            for symbol, ticker_obj in tickers_obj.tickers.items():
                last_price[symbol] = ticker_obj.fast_info["lastPrice"]
            return last_price
        except Exception as e:
            raise ValueError(f"Error fetching stock prices: {e}")
        
    @staticmethod    
    def update_portfolio_prices(portfolio):
        if not isinstance(portfolio, stockPortfolio):
            raise TypeError("Input must be a stockPortfolio instance")
        tickers = [stock.ticker for stock in portfolio.stocks.values()]
        last_prices = MarketData.fetch_stock_prices(tickers)
        for stock in portfolio.stocks.values():
            if stock.ticker in last_prices:
                stock.currPrice = last_prices[stock.ticker]
            else:
                raise ValueError(f"Price for ticker {stock.ticker} not found in fetched data")

        return portfolio
    