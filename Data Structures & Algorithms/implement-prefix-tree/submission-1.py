class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
class PrefixTree:

    def __init__(self):
        self.node=TrieNode()
        

    def insert(self, word: str) -> None:
        cur=self.node
        for i in word:
            j = ord(i) - ord("a")
            if cur.children[j]==None:
                cur.children[j]=TrieNode()
            cur=cur.children[j]
        cur.endOfWord=True





    def search(self, word: str) -> bool:
        cur=self.node
        for i in word:
            j = ord(i) - ord("a")
            if cur.children[j]==None:
                return False
            cur=cur.children[j]
        return cur.endOfWord

        

    def startsWith(self, prefix: str) -> bool:
        cur=self.node
        for i in prefix:
            j = ord(i) - ord("a")
            if cur.children[j]==None:
                return False
            cur=cur.children[j]
        return True
        
        