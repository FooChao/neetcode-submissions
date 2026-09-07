class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevStock = - float('inf')
        prevTrans = 0
        prevNoTrans = 0
        for price in prices:
            nextStock = max(prevStock, prevNoTrans - price)
            nextTrans = prevStock + price
            nextNoTrans = max(prevNoTrans, prevTrans)
            prevStock, prevTrans, prevNoTrans = nextStock, nextTrans, nextNoTrans
        
        return max(prevStock, prevTrans, prevNoTrans)
        