class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        tally=[0]*len(words)
        vowels={'a':0,'e':0,'i':0,'o':0,'u':0}

        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                tally[i]+=1
                    
        prefix=[0]*len(words)
        total=0
        for i in range(len(tally)):
            total+=tally[i]
            prefix[i]=total
        res=[]
        for s, e in queries:

            if s == 0:

                res.append(prefix[e])

            else:

                res.append(prefix[e] - prefix[s-1])
        return res
            


        