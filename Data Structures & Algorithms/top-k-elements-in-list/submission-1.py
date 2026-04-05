class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums) + 1)]
        map = dict()
        for i in nums:
            map[i] = 1 + map.get(i, 0)
        for key, v in map.items():
            arr[v].append(key)

        res = []
        for i in range(len(arr) - 1, 0, -1):
            for j in arr[i]:
                res.append(j)
                if len(res) == k:
                    return res
        