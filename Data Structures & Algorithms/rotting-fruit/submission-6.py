class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lr,lc=len(grid),len(grid[0])
        nums=deque([])
        ff=0
        time=0
        dirc=[(0,1),(1,0),(-1,0),(0,-1)]
        seen=set()
        for i in range(lr):
            for j in range(lc):
                if grid[i][j]==2:
                    nums.append((i,j))
                if grid[i][j]==1:
                    ff+=1
        if ff == 0:
            return 0

        
        kk=len(nums)
        while nums:

            r,c=nums.popleft()
            seen.add((r,c))
            for p,q in dirc:
                rn,cn=r+p,c+q
                if 0<=rn<lr and 0<=cn<lc and (rn,cn) not in seen:
                    
                    if grid[rn][cn]==1:
                        nums.append((rn,cn))
                        grid[rn][cn]=2
                        ff-=1
            kk-=1
            
            if kk==0:
                kk=len(nums)
                time+=1
                if ff==0:
                    return time
            
        return -1
            
                    

                




        