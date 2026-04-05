
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        q = deque([beginWord])
        visit = {word: False for word in wordList}
        visit[beginWord] = True
        level = 1
        
        def wordMatch(w):
            charArr = list(w)
            for i in range(len(charArr)):
                original_char = charArr[i]
                for j in range(26):
                    ch = chr(ord('a') + j)
                    if ch != original_char:
                        charArr[i] = ch
                        new_word = ''.join(charArr)
                        if new_word in wordList and not visit[new_word]:
                            q.append(new_word)
                            visit[new_word] = True
                charArr[i] = original_char

        while q:
            n = len(q)
            for i in range(n):
                word = q.popleft()
                if word == endWord:
                    return level
                wordMatch(word)
            level += 1
        
        return 0
