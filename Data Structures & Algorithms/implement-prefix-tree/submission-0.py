class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.children = [None] * 26


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        crawler = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            if crawler.children[idx] is None:
                crawler.children[idx] = TrieNode()
            crawler = crawler.children[idx]
        crawler.isEndOfWord = True

    def search(self, word: str) -> bool:
        crawler = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            if crawler.children[idx] is None:
                return False
            crawler = crawler.children[idx]
        return crawler.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        crawler = self.root
        for ch in prefix:
            idx = ord(ch) - ord("a")
            if crawler.children[idx] is None:
                return False
            crawler = crawler.children[idx]
        return True