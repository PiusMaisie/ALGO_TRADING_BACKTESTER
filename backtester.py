from indicators import TechnicalIndicators

class Backtester:
    """
    Simulates historical trade execution based on moving average crossovers,
    tracks portfolio equity, and calculates basic performance outcomes.
    """
    def __init__(self, initial_balance: float, prices: list[float], short_period: int = 3, long_period: int = 5):
        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.prices = prices
        self.short_period = short_period
        self.long_period = long_period
        self.trades = []
        self.equity_curve = [initial_balance]

    def run_backtest(self) -> dict:
        """
        Executes the backtesting simulation loop across historical price series.
        """
        if len(self.prices) < self.long_period:
            print("Error: Historical price data length is shorter than the long period indicator.")
            return {}

        # 1. Compute indicator series
        short_sma = TechnicalIndicators.simple_moving_average(self.prices, self.short_period)
        long_sma = TechnicalIndicators.simple_moving_average(self.prices, self.long_period)

        # To align short_sma with long_sma (since short_sma has more data points), 
        # we calculate the index offset:
        offset = len(short_sma) - len(long_sma)

        position_open = False
        entry_price = 0.0

        # 2. Simulation loop across time steps
        for i in range(len(long_sma)):
            s_val = short_sma[i + offset]
            l_val = long_sma[i]
            # Match current price with the index of the long moving average window
            current_price = self.prices[i + self.long_period - 1]

            # Strategy Rule: Bullish Crossover (Short SMA crosses ABOVE Long SMA) -> BUY
            if s_val > l_val and not position_open:
                position_open = True
                entry_price = current_price
                self.trades.append({"action": "BUY", "price": entry_price})

            # Strategy Rule: Bearish Crossover (Short SMA crosses BELOW Long SMA) -> SELL/CLOSE
            elif s_val < l_val and position_open:
                position_open = False
                exit_price = current_price
                
                # Calculate simple profit/loss simulation (mock profit multiplier)
                trade_pnl = (exit_price - entry_price) * 1000  
                self.balance += trade_pnl
                self.equity_curve.append(round(self.balance, 2))
                
                self.trades.append({"action": "SELL", "price": exit_price, "pnl": round(trade_pnl, 2)})

        # 3. Compile performance summary
        net_profit = self.balance - self.initial_balance
        return {
            "initial_balance": self.initial_balance,
            "final_balance": round(self.balance, 2),
            "net_profit": round(net_profit, 2),
            "total_trades": len(self.trades)
        }
        


if __name__ == "__main__":
    # Mock historical price series showing an uptrend then a downtrend
    historical_prices = [1.1000, 1.1020, 1.1050, 1.1080, 1.1060, 1.1040, 1.1010, 1.1030, 1.1070]
    
    backtester = Backtester(initial_balance=5000.0, prices=historical_prices, short_period=2, long_period=4)
    results = backtester.run_backtest()
    
    print("--- Backtest Results ---")
    for key, value in results.items():
        print(f"{key}: {value}")
    