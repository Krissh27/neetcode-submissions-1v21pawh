class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo=[[-1]*len(text1) for i in range(len(text2))]

        def dfs(i,j):
            if i>len(text1)-1 or j>len(text2)-1:
                return 0
            if text1[i]==text2[j]:
                memo[j][i] = 1 + dfs(i+1, j+1)
                return memo[j][i]

            if memo[j][i]!= -1:
                return memo[j][i]
            memo[j][i]=max(dfs(i+1,j),dfs(i,j+1))
            return memo[j][i]
        return dfs(0,0)
        