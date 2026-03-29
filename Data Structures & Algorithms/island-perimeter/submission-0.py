class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        lr,lc=len(grid),len(grid[0])
        def dfs(r,c):
            if r>=lr or r<0 or c>=lc or c<0 :
                return 1
            if grid[r][c] == 0:
                return 1
            if grid[r][c] == -1:
                return 0
            grid[r][c]=-1
            return dfs(r+1,c)+ dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        for i in range(lr):
            for j in range(lc):
                if grid[i][j]==1:
                    return dfs(i,j)
            
        