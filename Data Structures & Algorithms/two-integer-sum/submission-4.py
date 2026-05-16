class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict()
        for i in range(len(nums)):
            val = target - nums[i]
            if val in mp:
                return [mp.get(val), i]
            mp[nums[i]] = i
        return []
