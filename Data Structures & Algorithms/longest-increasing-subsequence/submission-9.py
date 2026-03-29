class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo={}
        n=len(nums)
        def dfs(i,j):
            if j==n:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if i==-1:
                memo[(i,j)]= max(dfs(i,j+1),1+dfs(j,j+1))
                return memo[(i,j)]
            if nums[i]<nums[j]:
                memo[(i,j)]=  max(1+dfs(j,j+1),dfs(i,j+1))
                return memo[(i,j)]
            memo[(i,j)]= dfs(i,j+1)
            return memo[(i,j)]
        return dfs(-1,0)

        