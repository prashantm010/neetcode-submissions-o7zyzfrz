class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        q = deque([beginWord])
        visit = {x:False for x in wordList}
        visit[beginWord] = True
        l = 1

        def match(word):
            wordArr = list(word)
            for c in range(len(wordArr)):
                og = wordArr[c]
                for i in range(26):
                    nc = chr(ord('a') + i)
                    if nc != og:
                        wordArr[c] = nc
                        nWord = ''.join(wordArr)
                        if nWord in wordList and not visit[nWord]:
                            q.append(nWord)
                            visit[nWord] = True
                wordArr[c] = og

        while q:
            n = len(q)
            for i in range(n):
                word = q.popleft()
                if word == endWord:
                    return l
                match(word)
            l += 1
        return 0

        