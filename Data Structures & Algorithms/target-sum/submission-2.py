class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(t,i):
            if i>=len(nums) and t==target:
                return 1
            if i>=len(nums):
                return 0
            return dfs(t+nums[i],i+1)+dfs(t-nums[i],i+1)
        return dfs(0,0)
            