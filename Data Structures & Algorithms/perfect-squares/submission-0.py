class Solution:
    def numSquares(self, n: int) -> int:
        nums=[-1]*n
        def dfs(i):
            if i>n:
                return float('inf')
            if i==n:
                return 0
            kk=float('inf')
            if nums[i]!=-1:
                return nums[i]
            for j in range(1,math.ceil(n**1/2)+1):
                kk=min(dfs(i+j**2)+1,kk)
            nums[i]=kk
            return kk
        z=dfs(0)
        
        return z

        