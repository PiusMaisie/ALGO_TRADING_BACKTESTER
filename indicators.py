class TechnicalIndicators:
    """
    Computes mathematical technical indicators from historical price series 
    to assist with trading signal generation.
    """
    
    @staticmethod      # @abstractmethod: This is the magic decorator. It registers this 
                        # specific method as mandatory. If any child class inherits from 
                        # Vehicle(car, bycicle,motor,truck) and doesn't write a start_engine() method, Python 
                        # will throw a TypeError when you try to create that child object.
                        # The @staticmethod decorator tells Python: "This function doesn't use 'self' or 'cls'. 
                        # It is just a self-contained math utility living inside this class."
                        

                       
    def simple_moving_average(prices: list[float], period: int) -> list[float]:
        """
        Calculates the Simple Moving Average (SMA) for a list of closing prices.
        
        Args:
            prices (list): Historical price series (e.g., daily or hourly closing prices).
            period (int): The number of periods for the moving average (e.g., 20 or 50).
            
        Returns:
            list: A list of moving average values.
        """
        # Safety check: if we don't have enough data points for the period, return an empty list
        if len(prices) < period:
            return []
        
        sma_values = []
        
        # Slide a window of size 'period' across the prices list
        for i in range(len(prices) - period + 1):
            window = prices[i : i + period]
            average = sum(window) / period
            sma_values.append(round(average, 4))
            
        return sma_values


if __name__ == "__main__":
    # Mock closing prices for a currency pair or stock over 6 days
    mock_prices = [1.1000, 1.1050, 1.1020, 1.1080, 1.1100, 1.1120]
    
    # Calculate a 3-period SMA
    sma_result = TechnicalIndicators.simple_moving_average(mock_prices, period=3)
    
    print("Mock Prices:", mock_prices)
    print("3-Period SMA Results:", sma_result)      #How the calculation is done
                                                    # at i =  0 period is 3 so prices from 0,1,2
                                                    # so sum(1.10,1.105,1.102) /average
                                                    # i = 1 period is still 3 so price from 1,2,3
                                                    # so sum(1.1050, 1.1020, 1.1080) /3 ......cc