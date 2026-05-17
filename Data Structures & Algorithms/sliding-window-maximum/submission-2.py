class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = []
        res = []

        for i in range(len(nums)):
            while dq and dq[0] <= i - k:
                dq.pop(0)
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
