class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp={}
        def dfs(i,j):
            if i>=n:
                return 0
            k=0
            if (i,j) in dp:
                return dp[(i,j)]
            if j==-1 or nums[i]>nums[j]:
                k=1+dfs(i+1,i)
            skip=dfs(i+1,j)
            dp[(i,j)]= max(k,skip)
            return dp[(i,j)]
        return dfs(0,-1)
        