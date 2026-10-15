class RiskManager:
    """
    Manages account risk, calculates risk per trade in dollars and determines
    precise position/lot size  for trading.
    """

    def __init__(self, account_balance: float,risk_percentage: float = 1.0):
        """
        Initializes the RiskManager with account balance and risk percentage.
        :param account_balance: The total account balance in dollars.
        :param risk_percentage: The percentage of the account to risk per trade (default is 1%).
        """
        self.account_balance = account_balance
        self.risk_percentage = risk_percentage

    def calculate_risk_amount(self) -> float:
        """
        Calculates the dollar amount to risk per trade based on account balance
        and risk percentage.:return: The dollar amount to risk per trade.
        """
        risk_amount =  self.account_balance * (self.risk_percentage / 100)
        return round(risk_amount, 2)

    def calculate_position_size(self,stop_loss_pips: float,pip_value_per_lot: float = 10.0) -> float:
        """
        Calculates the position size (in lots) based on the risk amount, stop loss in pips,
        and pip value per lot.
        Arguments:
            stop_loss_pips: The stop loss in pips for the trade.
            pip_value_per_lot: The value of one pip per standard lot (default is $10 for major USD pairs).
        Return:
            Float:Recommended position size in lots to 2 decimal places.
        """
        if stop_loss_pips <= 0:
            raise ValueError("Stop loss pips must be greater than zero.")
        
        risk_dollar = self.calculate_risk_amount()
        risk_per_standard_lot = (stop_loss_pips * pip_value_per_lot)

        if risk_per_standard_lot == 0:
            return 0.0  # Avoid division by zero if stop_loss_pips is zero
        standard_lots = risk_dollar / risk_per_standard_lot

        return round(standard_lots, 2)



#"------------------Testing part 1-------------------"
if __name__ == "__main__":
    Exness_Account = RiskManager(5000.00,1)
    Aqua_funded_Account = RiskManager(1000.00,2)
    Alpha_Capital = RiskManager(2500.00,3)

    A1 = Exness_Account.calculate_risk_amount()
    A2 = Aqua_funded_Account.calculate_risk_amount()
    A3 = Alpha_Capital.calculate_risk_amount()

    print(f"\n=============================================")
    print(f"-----------Risk Management Test--------------")
    print(f"=============================================")
    print(f"\nYou risk amount per trade for Exness account is ${A1:.2f}")
    print(f"Your risk amount per trade for Aqua Funded Account is ${A2:.2f}")
    print(f"Your risk amount per trade for Alpha Capital is ${A3:.2f}")

    Lot_1 = Exness_Account.calculate_position_size(50,10)
    Lot_2 = Aqua_funded_Account.calculate_position_size(20,10)
    Lot_3 =  Alpha_Capital.calculate_position_size(30,10)

    print(f"\nLot size of {Lot_1:.2f} is recommended for Exness Account.")
    print(f"Lot size of {Lot_2:.2f} is recommended for Aqua Funded Account.")
    print(f"Lot size of {Lot_3:.2f} is recommended for Alpha Capital.")





