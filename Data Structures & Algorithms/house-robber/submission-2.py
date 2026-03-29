class Solution:
    def rob(self, nums: List[int]) -> int:
        kk=len(nums)
        num=[-1]*kk
        def dfs(n):
            if n>=kk:
                return 0
            if num[n] != -1:          
                return num[n]
            num[n]=max(nums[n]+ dfs(n+2),dfs(n+1))

            

            return num[n]
        return dfs(0)
            


