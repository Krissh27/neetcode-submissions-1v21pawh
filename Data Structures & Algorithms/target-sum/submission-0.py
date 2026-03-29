class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(s1,s2,i):
            if i>=len(nums) and (s1-s2)==target:
                return 1
            if i>=len(nums):
                return 0
            return dfs(s1+nums[i],s2,i+1)+dfs(s1,s2+nums[i],i+1)
        return dfs(0,0,0)
            