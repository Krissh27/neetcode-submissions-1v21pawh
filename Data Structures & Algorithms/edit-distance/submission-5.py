class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1=len(word1)
        w2=len(word2)
        memo=[0]*(w1+1) 
        
        for i in range(len(word1)):
            memo[i]=w1-i



        
        for i in range(w2-1,-1,-1):
            curr=[0]*(w1+1)
            curr[w1]=w2-i 
            for j in range(w1-1,-1,-1):
                if word1[j]==word2[i]:
                    curr[j]=memo[j+1]
                else:
                    curr[j]=1+min(memo[j+1],memo[j],curr[j+1])
            memo=curr
        return memo[0]
        