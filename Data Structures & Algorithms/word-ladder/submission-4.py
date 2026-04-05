class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Convert wordList to a set for O(1) lookups
        wordSet = set(wordList)
        q = deque()
        visits = set()
        q.append(beginWord)
        visits.add(beginWord)

        def watchWord(word):
            charArr = list(word)
            for i in range(len(charArr)):
                og_char = charArr[i]
                for j in range(26):
                    new_char = chr(ord('a') + j)
                    charArr[i] = new_char
                    newWord = ''.join(charArr)
                    if newWord in wordSet and newWord not in visits:
                        visits.add(newWord)
                        q.append(newWord)
                
                charArr[i] = og_char

        level = 1
        while q:
            n = len(q)
            for _ in range(n):
                word = q.popleft()
                if word == endWord:
                    return level
                watchWord(word)
            level += 1
        
        return 0