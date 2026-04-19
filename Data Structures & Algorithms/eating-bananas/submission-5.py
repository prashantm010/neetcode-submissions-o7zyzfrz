class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def canEat(k):
            total_hours = sum((p + k - 1) // k for p in piles)
            return total_hours <= h

        while l <= r:
            m = (l + r) // 2

            if canEat(m):
                r = m - 1
            else:
                l = m + 1

        return l