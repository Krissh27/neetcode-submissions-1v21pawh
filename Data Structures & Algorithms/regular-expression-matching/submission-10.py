class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(s)
        nn=len(p)
        memo={}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==-1 and (j==-1):
                return True
            if j<0:
                return False
            if i<0:
                if p[j]=="*":
                    return dfs(i,j-2)
                return False
            
            if p[j]=="." or p[j]==s[i]:
                memo[(i,j)]= dfs(i-1,j-1)
                return memo[(i,j)]
            if p[j]=="*":
                if j>0 and p[j - 1] == s[i] or p[j - 1] == ".":
                    memo[(i,j)]= dfs(i,j-2) or dfs(i-1,j)
                    return memo[(i,j)]
                memo[(i,j)]= dfs(i,j-2)
                return memo[(i,j)]
                
            return False
            
        return dfs(n-1,nn-1)
            
        