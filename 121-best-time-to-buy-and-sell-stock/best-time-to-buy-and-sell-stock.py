class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_future = 0
        max_profit = 0
        
        for price in reversed(prices):
            max_future = max(max_future, price)       
            max_profit = max(max_profit, max_future - price)
        
        return max_profit
