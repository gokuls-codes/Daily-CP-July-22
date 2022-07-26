class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        n = len(prices)
        
        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]
                
            if max_profit < prices[i] - min_price:
                max_profit = prices[i] - min_price
                
        return max_profit