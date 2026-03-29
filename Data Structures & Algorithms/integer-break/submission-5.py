class Solution:
    def integerBreak(self, n: int) -> int:
        nums=[-1]*(n+1)
        def dfs(i):
            if i==n:
                return 1
            if i>n:
                return 0
            kk=-1
            if nums[i]!=-1:
                return nums[i]
            for j in range(1,n-i+1):
                if j==n:
                    continue
                kk=max(j*dfs(i+j),kk)
            nums[i]=kk
            
            return kk
        return dfs(0)

            


            
        