class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0, len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    sum = nums[l] + nums[r] + nums[i]
                    if sum < 0:
                        l += 1
                    elif sum > 0:
                        r -= 1
                    else:
                        result.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        return result