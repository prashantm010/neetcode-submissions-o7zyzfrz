class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        ans = 0
        cMap = dict()
        for j in range(len(s)):
            cMap[s[j]] = 1 + cMap.get(s[j], 0)
            while ((j - i + 1) - max(cMap.values()) > k):
                cMap[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans