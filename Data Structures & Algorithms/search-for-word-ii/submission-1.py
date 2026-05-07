class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.isWord = False

    def addWord(self, word):
        curr = self
        for ch in word:
            c = ord(ch) - ord("a")
            if curr.child[c] == None:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or (r, c) in visit:
                return

            idx = ord(board[r][c]) - ord("a")
            if node.child[idx] == None:
                return

            visit.add((r, c))
            node = node.child[idx]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)
