class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        zz=self.root
        for i in word:
            k=ord(i)-ord('a')
            if zz.children[k]==None:
                zz.children[k]=TrieNode()
            zz=zz.children[k]
        zz.endOfWord = True



    def search(self, word: str) -> bool:
        zz=self.root
        for i in word:
            k=ord(i)-ord('a')
            if zz.children[k]==None:
                return False
            zz=zz.children[k]
        return zz.endOfWord
        
        

    def startsWith(self, prefix: str) -> bool:
        zz=self.root
        for i in prefix:
            k=ord(i)-ord('a')
            if zz.children[k]==None:
                return False
            zz=zz.children[k]
        return True
        
        