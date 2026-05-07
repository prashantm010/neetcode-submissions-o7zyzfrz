class TreeNode:
    def __init__(self):
        self.child = [None] * 26
        self.endOfWord = False


class WordDictionary:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            c = ord(ch) - ord("a")
            if curr.child[c] == None:
                curr.child[c] = TreeNode()
            curr = curr.child[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(index, curr):
            for i in range(index, len(word)):
                ch = word[i]
                if ch == ".":
                    for char in curr.child:
                        if char and dfs(i + 1, char):
                            return True
                    return False
                else:
                    c = ord(ch) - ord("a")
                    if curr.child[c] == None:
                        return False
                    curr = curr.child[c]
            return curr.endOfWord

        return dfs(0, self.root)
