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
        arr=[0]*(n+1)
        back=0
        back2=0
        for i in range(n-1,-1,-1):
            temp=back
            back=max(nums[i]+back2,back)
            back2=temp

            
        return back





        