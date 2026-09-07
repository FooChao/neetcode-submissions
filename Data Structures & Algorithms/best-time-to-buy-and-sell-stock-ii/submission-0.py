class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        bestWithStock = - prices[0]
        bestNoStock = 0

        for i in range (1, len(prices)):
            prevBestNoStock = bestNoStock
            bestNoStock = max(bestNoStock, bestWithStock + prices[i])
            bestWithStock = max(bestWithStock , prevBestNoStock - prices[i])
        
        return max(bestWithStock, bestNoStock)
        