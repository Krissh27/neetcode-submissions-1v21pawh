class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        lr,lc=len(grid),len(grid[0])
        dirc=[(1,0),(0,1),(-1,0),(0,-1)]
        nums=deque([])
        for i in range(lr):
            for j in range(lc):
                if grid[i][j]==0:
                    nums.append((i,j))

      
        while nums:
            r1,c1=nums.popleft()
            for p,q in dirc:
                r=r1+p
                c=c1+q
                if 0<=r<lr and 0<=c<lc:
                    if grid[r][c]==2147483647:
                        grid[r][c]=grid[r1][c1]+1
                        nums.append((r,c))
        
        







        