def maxProfit(prices):
    if not prices or len(prices) == 1:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        # Update minimum purchase price
        min_price = min(min_price, price)
        # Calculate whether the current selling profit is greater
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

# example
prices = [7, 1, 5, 3, 6, 4]
result = maxProfit(prices)
print(result)  # output 5