class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cashe=[[-1]*len(grid[0]) for i in range(len(grid))]
        def dfs(i,j):
            if i ==len(grid)-1 and j==len(grid[0])-1:
                return grid[i][j]
            if i >=len(grid) or j>= len(grid[0]):
                return float('inf')
            if cashe[i][j]!=-1:
                return cashe[i][j]
            cashe[i][j]=grid[i][j]+min(dfs(i+1,j),dfs(i,j+1))
            return cashe[i][j]
        return dfs(0,0)
            
        
            

            



        