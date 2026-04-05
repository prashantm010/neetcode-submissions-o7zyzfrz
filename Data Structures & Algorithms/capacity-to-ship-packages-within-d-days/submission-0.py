class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap, max_cap = max(weights), sum(weights)

        def canShip(cap):
            ship_needed = 1
            current = 0
            for w in weights:
                if current + w > cap:
                    ship_needed += 1
                    current = 0
                current += w
            return ship_needed <= days

        while min_cap < max_cap:
            cap = (min_cap + max_cap) // 2
            if canShip(cap):
                max_cap = cap
            else:
                min_cap = cap + 1

        return min_cap
