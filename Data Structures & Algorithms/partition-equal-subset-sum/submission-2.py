class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        traget=sum(nums)
        dp=[[-1]*(traget+1) for i in range(len(nums))]

        
        if traget%2!=0:
            return False
        def dfs(i,t):
            if t ==0 and i<len(nums):
                return True
            if t<0:
                return False
            if i>=len(nums):
                return False
            if dp[i][t]!=-1:
                return dp[i][t]
            dp[i][t]=dfs(i+1,t-nums[i]) or dfs(i+1,t)


            return dp[i][t]
        return dfs(0,traget//2)


            
            

            
            
        