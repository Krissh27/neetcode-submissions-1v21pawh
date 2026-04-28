class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        memo={}
        def dfs(l,r,flag):
            if l>r:
                return 0
            if (l,r,flag) in memo:
                return memo[l,r,flag]
            if flag:
                
                memo[l,r,flag]= max(nums[l]+dfs(l+1,r,not flag),nums[r]+dfs(l,r-1,not flag))
            else:
                memo[l,r,flag]= min(dfs(l+1,r,not flag),dfs(l,r-1,not flag))
            return memo[l,r,flag]
        if dfs(0,len(nums)-1,True)>=sum(nums)//2+1:
            return True
        return False



        
        