class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            maxProfit = max(prices[i] - start, maxProfit)
            start = min(prices[i], start)
        return maxProfit
