class Solution:
    # @param prices, a list of integer
    # @return an integer
    
    def maxProfit(self, prices):
        profit = [0]
        high_price = 0
        low_price = 0
        if len(prices) > 1:
            if prices[0] < prices[1]:
                low_price = prices[0]
                high_price = prices[1]
            else:
                low_price = prices[1]
            for i in range(1,len(prices)):
                if prices[i] < low_price:
                    profit.append(high_price - low_price)
                    low_price = prices[i]
                    high_price = 0
                if prices[i] > high_price:
                    high_price = prices[i]
            profit.append(high_price - low_price)
        return max(max(profit), 0)