class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m=len(obstacleGrid[0]),len(obstacleGrid)
        cashe=[[-1]*n for i in range(m)]

        def dfs(m1,n1):
            if m1>=m or n1>=n or obstacleGrid[m1][n1]==1 :
                return 0
            if m1==m-1 and n1==n-1:
                return 1
            
            if cashe[m1][n1]!=-1:
                return cashe[m1][n1]
            cashe[m1][n1]=dfs(m1+1,n1)+dfs(m1,n1+1)
            return cashe[m1][n1]


        return  dfs(0,0)  