class TrieNode:
    def __init__(self):
        self.listi=[None]*26
        self.status=False

class WordDictionary:

    def __init__(self):
        self.head=TrieNode()
        

    def addWord(self, word: str) -> None:
        cur=self.head
        for c in word:
            j= ord(c)-ord("a")
            if cur.listi[j]==None:
                cur.listi[j]=TrieNode()
            cur=cur.listi[j]
        cur.status=True


    def search(self, word: str) -> bool:

        def dfs(i,node):
            
            if i ==len(word):
                return node.status
            


            if word[i]==".":
                for j in node.listi:
                    if j and dfs(i+1,j):
                        return True
                return False
            j=ord(word[i])-ord("a")



            if node and node.listi[j]!=None:
                return dfs(i+1,node.listi[j])
            return False


        return dfs(0,self.head)
            


        
