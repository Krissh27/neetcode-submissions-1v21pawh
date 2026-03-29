class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lr,lc=len(grid),len(grid[0])
        def dfs(r,c):
            if r>=lr or r<0 or c>=lc or c<0 :
                return 
            if grid[r][c] == "0":
                return 
            if grid[r][c] == "-1":
                return 
            grid[r][c]="-1"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        island=0
        
        for i in range(lr):
            for j in range(lc):
                if grid[i][j]=="1":
                    dfs(i,j)
                    island+=1
        return island
            
        