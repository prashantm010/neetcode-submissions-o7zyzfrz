class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        self.n = len(s)
        max_word_len = max(len(word) for word in wordDict)
        self.dp = [False] * (self.n + 1)
        self.dp[self.n] = True
        
        for i in range(self.n - 1, -1, -1):
            for length in range(1, min(max_word_len, self.n - i) + 1): 
                if s[i:i+length] in wordSet and self.dp[i + length]:
                    self.dp[i] = True
                    break
            
        return self.dp[0]
