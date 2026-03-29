class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m=len(obstacleGrid[0]),len(obstacleGrid)
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        cashe=[0]*n 
        cashe[n-1]=1

        for i in range(m-1,-1,-1):
            temp=[0]*n
            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j]==1:
                    temp[j]=0
                    continue
                k=0
                if i == m-1 and j == n-1:
                    temp[j] = 1
                    continue

                if j+1<n:
                    k+=temp[j+1]
                
                k+=cashe[j]
                temp[j]=k
            cashe=temp
        return cashe[0]










           