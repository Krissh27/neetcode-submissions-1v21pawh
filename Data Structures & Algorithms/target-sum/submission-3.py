class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo=dict()
        def dfs(t,i):
            if i>=len(nums) and t==target:
                return 1
            if i>=len(nums):
                return 0
            if (t,i) in memo:
                return memo[(t,i)]
            memo[(t,i)]=dfs(t+nums[i],i+1)+dfs(t-nums[i],i+1)
            return memo[(t,i)] 
        return dfs(0,0)
            