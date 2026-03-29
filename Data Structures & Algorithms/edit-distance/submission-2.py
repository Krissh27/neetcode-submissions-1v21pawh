class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo=[[-1]*len(word1) for i in range(len(word2))]
        def dfs(i,j):
            if j==len(word2) and i==len(word1):
                return 0
            if i==len(word1):
                return len(word2[j:])
            if j==len(word2):
                return len(word1[i:])
            if memo[j][i]!=-1:
                return memo[j][i]
            if word1[i]==word2[j]:
                memo[j][i]= dfs(i+1,j+1)
                return memo[j][i]
            memo[j][i]= 1+min(dfs(i+1,j+1),dfs(i+1,j),dfs(i,j+1))
            return memo[j][i]
        return dfs(0,0)
        