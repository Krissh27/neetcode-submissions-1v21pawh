class TrieNode:
    def __init__(self):
        self.dicts={}
        self.end=False
        


class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

        

    def insert(self, word: str) -> None:
        curr=self.root
        for i in word:
            if i not in curr.dicts:
                curr.dicts[i]=TrieNode()
            curr=curr.dicts[i]
        curr.end=True

            



    def search(self, word: str) -> bool:
        curr=self.root
        for i in word:
            if i not in curr.dicts:
                return False
            curr=curr.dicts[i]
        if curr.end==True:
            return True
        return False

        
            



        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for i in prefix:
            if i not in curr.dicts:
                return False
            curr=curr.dicts[i]
        return True
        
        