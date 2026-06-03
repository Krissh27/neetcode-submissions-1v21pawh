class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        com={}
        for i in range(len(order)):
            com[order[i]]=i
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            for z in range(len(w1)):
                if z==len(w2):
                    return False
                if w1[z] != w2[z]:
                    if com[w1[z]]>com[w2[z]]:
                        return False
                    break
                    
        return True



