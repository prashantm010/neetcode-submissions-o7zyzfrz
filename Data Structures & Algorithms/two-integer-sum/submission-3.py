class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for i, n in enumerate(nums):
            map[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in map and map[diff] != i:
                return [i, map[diff]]
        