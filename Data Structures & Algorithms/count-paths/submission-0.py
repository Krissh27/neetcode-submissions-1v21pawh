class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cashe=[[-1]*n for i in range(m)]

        def dfs(m1,n1):
            if m1==m-1 and n1==n-1:
                return 1
            if m1>=m or n1>=n:
                return 0
            return dfs(m1+1,n1)+dfs(m1,n1+1) 

        return  dfs(0,0)        
        