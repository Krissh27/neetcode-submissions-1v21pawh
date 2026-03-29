class Solution:
    def jump(self, nums: List[int]) -> int:
        dp={}
        n=len(nums)
        def dfs(i):
            res=float('inf')
            if i>=n-1:
                return 0
            if i in dp:
                return dp[i]
            for ii in range(i+1,min(i+nums[i]+1,n)):
                res= min(res,1+dfs(ii))
            dp[i]=res
            return res
        return dfs(0)
            

        