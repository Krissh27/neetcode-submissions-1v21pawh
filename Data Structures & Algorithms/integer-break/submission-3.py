class Solution:
    def integerBreak(self, n: int) -> int:
        nums=[-1]*(n+1)
        def dfs(i,depth):
            if i==n and depth>1:
                return 1
            elif i==n and depth==1:
                return 0
            if i>n :
                return 0
            
            if nums[i]!=-1:
                return nums[i]
            kk=-1
            for j in range(1,n-i+1):
                kk=max(j*dfs(i+j,depth+1),kk)
            nums[i]=kk
            
            return kk
        return dfs(0,0)

            


            
        