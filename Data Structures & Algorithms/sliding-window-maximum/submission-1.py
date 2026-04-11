from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices (not values)
        res = []

        for i in range(len(nums)):

            # ❗ 1. Remove indices out of current window
            # Window range = [i-k+1, i]
            # So remove anything <= i-k
            while dq and dq[0] <= i - k:
                dq.popleft()

            # ❗ 2. Maintain decreasing order in deque
            # Remove all smaller elements from back
            # because they can never be max if current element is bigger
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()

            # Add current index
            dq.append(i)

            # ❗ 3. Start recording result when window is full
            if i >= k - 1:
                # Front of deque always has max element index
                res.append(nums[dq[0]])

        return res