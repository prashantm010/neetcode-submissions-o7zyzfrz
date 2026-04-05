class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        pivot = 0
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        res = self.binary_search(nums, target, 0, pivot - 1)
        if res != -1:
            return res
        else:
            return self.binary_search(nums, target, pivot, len(nums) - 1)

    def binary_search(self, nums, target, l, r):
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
