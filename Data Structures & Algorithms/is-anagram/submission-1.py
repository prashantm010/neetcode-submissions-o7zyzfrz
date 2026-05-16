class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a1 = dict()
        for a in s:
            a1[a] = a1.get(a, 0) + 1
        
        a2 = dict()
        for b in t:
            a2[b] = a2.get(b, 0) + 1

        return a1 == a2
        