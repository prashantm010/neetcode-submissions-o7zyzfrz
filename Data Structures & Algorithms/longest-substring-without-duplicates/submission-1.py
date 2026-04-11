class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strSet = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in strSet:
                strSet.remove(s[l])
                l+=1
            strSet.add(s[i])
            res = max(res, i - l + 1)
        return res