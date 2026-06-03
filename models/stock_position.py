class stockPos:
    def __init__(self, ticker, shares, boughtPrice , currPrice):
        
        if (shares <= 0 or boughtPrice < 0 or currPrice < 0):
            raise ValueError("Shares, bought price and current price must be non-negative.")
        if (ticker == ""):
            raise ValueError("Ticker cannot be empty.")
        self.ticker = ticker
        self.shares = shares
        self.boughtPrice = boughtPrice
        self.currPrice = currPrice 
    
    def to_dict(self):
        return {
            "ticker" : self.ticker,
            "shares" : self.shares,
            "boughtPrice" : self.boughtPrice,
            "currPrice" : self.currPrice
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f"Ticker: {self.ticker}, Shares: {self.shares}, Bought price: {self.boughtPrice}, Current price: {self.currPrice}"
    
    def cost_basis(self):
        return self.shares * self.boughtPrice
    
    def market_value(self):
        return self.shares * self.currPrice
    
    def pnl(self):
        return self.shares * (self.currPrice - self.boughtPrice)
    