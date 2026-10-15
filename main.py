from risk import RiskManager
from backtester import Backtester

def display_banner():
    print("=" * 55)
    print("   ALGORITHMIC TRADING BACKTESTER & RISK CALCULATOR   ")
    print("=" * 55)

def main():
    display_banner()
    
    # Sample historical price data (mock series representing currency pair closing prices)
    sample_prices = [
        1.0850, 1.0865, 1.0880, 1.0870, 1.0860, 
        1.0890, 1.0910, 1.0905, 1.0925, 1.0940,
        1.0930, 1.0915, 1.0900, 1.0920, 1.0950
    ]

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Calculate Position & Risk Sizing")
        print("2. Run Moving Average Crossover Backtest")
        print("3. Exit Application")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == "1":
            print("\n--- Risk Management Calculator ---")
            try:
                balance = float(input("Enter account balance ($): "))
                risk_pct = float(input("Enter risk percentage per trade (%): "))
                stop_loss = float(input("Enter stop loss distance (pips): "))
                
                manager = RiskManager(account_balance=balance, risk_percentage=risk_pct)
                risk_amt = manager.calculate_risk_amount()
                lot_size = manager.calculate_position_size(stop_loss_pips=stop_loss)
                
                print(f"\n=====[Results]=====")
                print(f"Allowed Risk Amount: ${risk_amt:.2f}")
                print(f"Recommended Position Size: {lot_size:.2f} standard lots")
            except ValueError as e:
                print(f"Invalid input: {e}")
                
        elif choice == "2":
            print("\n--- Running Backtest Simulation ---")
            try:
                balance = float(input("Enter initial balance for simulation ($): "))
                short_p = int(input("Enter short MA period (e.g., 2): "))
                long_p = int(input("Enter long MA period (e.g., 4): "))
                
                backtester = Backtester(
                    initial_balance=balance, 
                    prices=sample_prices, 
                    short_period=short_p, 
                    long_period=long_p
                )
                results = backtester.run_backtest()
                
                if results:
                    print("\n=====[Backtest Performance Summary]=====")
                    for key, value in results.items():
                        print(f"• {key.replace('_', ' ').title()}: {value}")
            except ValueError as e:
                print(f"Invalid input: {e}")
                
        elif choice == "3":
            print("\nShutting down Algorithmic Trading Backtester. Excellent work building this project!")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()