class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp={}
        if n==1:
            return nums[0]
        def dfs(i,flag):
            if (flag and i>=n-1) or (not flag and i>=n):
                return 0
            if (flag,i) in dp:
                return dp[(flag,i)]
            
            dp[(flag,i)]= max(nums[i]+dfs(i+2,flag),dfs(i+1,flag))
            return dp[(flag,i)]
        return max(dfs(0,True),dfs(1,False))
        