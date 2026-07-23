class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=0
       
        n=len(nums)
        def dfs(i,k):
            nonlocal res
            if i >=n:
                res+=k
                return
            
            dfs(i+1,k)
            k=k^nums[i]
            dfs(i+1,k)
            return 
        dfs(0,0)
        return res




            
            
            
            
        