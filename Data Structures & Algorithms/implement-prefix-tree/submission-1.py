class TreeNode:
    def __init__(self):
        self.child = [None] * 26
        self.endOfWord = False


class PrefixTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            c = ord(char) - ord("a")
            if current.child[c] == None:
                current.child[c] = TreeNode()

            current = current.child[c]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            c = ord(char) - ord("a")
            if curr.child[c] == None:
                return False
            curr = curr.child[c]
        if curr.endOfWord == False:
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            c = ord(char) - ord("a")
            if curr.child[c] == None:
                return False
            curr = curr.child[c]

        return True
