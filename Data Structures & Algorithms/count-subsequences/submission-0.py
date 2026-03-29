class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def dfs(i,j,ss):
            if j==len(t):
                return 1

            if i>=len(s) or j>=len(t):
                return 0
            
            if s[i]==t[j]:
                return dfs(i+1,j+1,ss+s[i])+dfs(i+1,j,ss)
            return dfs(i+1,j,ss)
        return dfs(0,0,"")

        