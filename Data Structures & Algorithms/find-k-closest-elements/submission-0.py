class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        mp = dict()
        for i in arr:
            diff = abs(x - i)
            if diff in mp:
                mp[diff].append(i)
            else:
                mp[diff] = [i]
        mp = dict(sorted(mp.items()))
        count = 0
        res = []
        for key, value in mp.items():
            for b in value:
                if count >= k:
                    break
                res.append(b)
                count += 1
        return sorted(res)
        