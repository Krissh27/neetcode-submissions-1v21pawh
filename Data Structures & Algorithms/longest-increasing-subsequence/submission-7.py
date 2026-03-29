class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        def dfs(i,j):
            if j==n:
                return 0
            if i==-1:
                return max(dfs(i,j+1),1+dfs(j,j+1))
            if nums[i]<nums[j]:
                return max(1+dfs(j,j+1),dfs(i,j+1))
            return dfs(i,j+1)
        return dfs(-1,0)

        