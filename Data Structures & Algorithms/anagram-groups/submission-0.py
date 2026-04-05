class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        for i in strs:
            a = ''.join(sorted(i))
            if a not in map:
                res = []
            else:
                res = map[a]
            res.append(i)
            map[a] = res
        
        res = []
        for i in map:
            res.append(map[i])
        return res
        