class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lr=len(nums)
        maxi=1
        def dfs(i,j,length):
            nonlocal maxi
            if i>=lr:
                return 
            if nums[j]<nums[i]:
                
                maxi=max(maxi,length+1)
                dfs(i+1,i,length+1)
                dfs(i+1,j,length)
                return
                
            dfs(i+1,j,length)
            

            dfs(i+1,i,1)
        dfs(1,0,1)
        return maxi

            
                

        