class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevMinPrice = float('inf')
        currentMaxProfit = 0
        for price in prices:
            currentMaxProfit = max(currentMaxProfit, price - prevMinPrice)
            prevMinPrice = min(prevMinPrice, price)
        return currentMaxProfit