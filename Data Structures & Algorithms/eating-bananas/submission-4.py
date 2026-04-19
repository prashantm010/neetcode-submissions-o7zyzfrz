class Solution:
    def minEatingSpeed(self, piles: List[int], k: int) -> int:
        l, h = 1, max(piles)

        def canEat(n):
            total_hours = 0
            total_hours = sum((p+n-1)//n for p in piles)
            return total_hours <= k



        ans = h
        while l <= h:
            m = (l + h) // 2
            if canEat(m):
                ans = m
                h = m - 1
            else:
                l = m + 1
        return ans