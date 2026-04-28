class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[-1] * 2 for _ in range(len(nums))]
        if len(nums)==1:
            return nums[0]
        def dfs(i,flag):
            if (i>=n-1 and flag) or (i>=n and not flag):
                return 0
            if dp[i][flag] !=-1:
                return dp[i][flag]
            dp[i][flag]=max(dfs(i+2,flag)+nums[i],dfs(i+1,flag))
            return dp[i][flag]
        return max(dfs(0,1),dfs(1,0))

        