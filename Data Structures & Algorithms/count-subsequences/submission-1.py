class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cashe=[[-1]*len(s) for i in range(len(t))]
        
        def dfs(i,j,ss):
            
            if j==len(t):
                return 1


            if i>=len(s) or j>=len(t):
                return 0
            if cashe[j][i]!=-1:
                return cashe[j][i]
            
            if s[i]==t[j]:
                cashe[j][i]= dfs(i+1,j+1,ss+s[i])+dfs(i+1,j,ss)
                return cashe[j][i]
            cashe[j][i]= dfs(i+1,j,ss)
            return cashe[j][i]
        return dfs(0,0,"")

        