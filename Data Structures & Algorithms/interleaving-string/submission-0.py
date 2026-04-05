class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        result = []
        self.solve(s1, s2, "", result)
        return s3 in result
    
    def solve(self, s1, s2, current, result):
        if not s1 and not s2:
            result.append(current)
            return
        if s1:
            self.solve(s1[1:], s2, current + s1[0], result)
        if s2:
            self.solve(s1, s2[1:], current + s2[0], result)