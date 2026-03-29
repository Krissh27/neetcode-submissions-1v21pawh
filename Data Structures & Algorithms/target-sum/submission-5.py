class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        memo = [[-1] * (2*total_sum + 1) for _ in range(len(nums))]
        def dfs(t,i):
            if i>=len(nums) and t==target:
                return 1
            if i>=len(nums):
                return 0
            if memo[i][t+target] !=-1:
                return memo[i][t+target]
            memo[i][t+target]=dfs(t+nums[i],i+1)+dfs(t-nums[i],i+1)
            return memo[i][t+target] 
        return dfs(0,0)