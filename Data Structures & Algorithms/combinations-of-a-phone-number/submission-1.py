class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mp = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        def dfs(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            for c in mp[digits[i]]:
                dfs(i + 1, curr + c)
            
        if digits:
            dfs(0, "")
        return res