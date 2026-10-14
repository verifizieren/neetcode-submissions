from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.childs = 26 * [None]
        self.endOfWord = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            i = ord(char) - ord("a")
            if current.childs[i] == None:
                current.childs[i] = TrieNode()
            current = current.childs[i]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            i = ord(char) - ord("a")
            if current.childs[i]:
                current = current.childs[i]
            else:
                return False
        if current and current.endOfWord:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            i = ord(char) - ord("a")
            if current.childs[i]:
                current = current.childs[i]
            else:
                return False
        return True
        