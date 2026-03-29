class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def dfs(i,s1,s2):
            if i>=len(nums) and s1==s2:
                return True
            elif i>=len(nums) and s1!=s2:
                return False
            return dfs(i+1,s1+nums[i],s2) or dfs(i+1,s1,s2+nums[i])

        return dfs(0,0,0)
            
            
            
        