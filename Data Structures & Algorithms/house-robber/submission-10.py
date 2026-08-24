class Solution:
    def rob(self, nums: List[int]) -> int:
        '''class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        memo={}
        def dfs(i):
            if i>=n:
                return 0
            if i in memo:
                return memo[i]
            memo[i]=max(dfs(i+1), nums[i]+dfs(i+2))
            return memo[i]
        return dfs(0)'''
    
        n=len(nums)
        arr=[0]*(n+2)
        for i in range(n-1,-1,-1):
            arr[i]=max(arr[i+1],arr[i+2]+nums[i])
        return arr[0]





        