class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        k = 4
        nums = matchsticks
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort()
        if nums[0] > target:
            return False

        buckets = [0] * k

        def dfs(i):
            if i == len(nums):
                return True

            for j in range(k):
                if buckets[j] + nums[i] > target:
                    continue

                if j > 0 and buckets[j] == buckets[j - 1]:
                    continue

                buckets[j] += nums[i]
                if dfs(i + 1):
                    return True
                buckets[j] -= nums[i]

            return False

        return dfs(0)

