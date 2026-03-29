class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        sub=[]
        def transverse(val):
            if val>=len(nums):
                result.append(sub.copy())
                return 
            sub.append(nums[val])
            transverse(val+1)
            sub.pop()
            while (val+1)<len(nums) and nums[val]==nums[val+1]:
                val=val+1
            transverse(val+1)
        
        transverse(0)
        
        return result


        