class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        pr = 1
        for i in range(len(nums)):
            res[i] = pr
            pr = pr * nums[i]

        po = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= po
            po *= nums[i]
        return res
        