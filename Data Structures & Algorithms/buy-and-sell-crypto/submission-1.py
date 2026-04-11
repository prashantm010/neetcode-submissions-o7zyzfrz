class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = prices[0]
        n = len(prices)
        profit = 0
        for i in range(1, n):
            sell = prices[i] - s
            profit = max(profit, sell)
            s = min(s, prices[i])
        return profit