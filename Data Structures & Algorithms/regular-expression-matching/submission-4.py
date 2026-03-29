class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(s)
        nn=len(p)
        def dfs(i,j):
            if i==-1 and (j==-1):
                return True
            if j<0:
                return False
            if i<0:
                if p[j]=="*":
                    return dfs(i,j-2)
            if p[j]=="." or p[j]==s[i]:
                return dfs(i-1,j-1)
            if p[j]=="*":
                if p[j - 1] == s[i] or p[j - 1] == ".":
                    return dfs(i,j-2) or dfs(i-1,j)
                return dfs(i,j-2)
                
            return False
            
        return dfs(n-1,nn-1)
            
        