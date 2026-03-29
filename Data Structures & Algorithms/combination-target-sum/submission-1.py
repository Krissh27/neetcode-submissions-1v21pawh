class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        sub=[]
       
        def transverse(val,sum1):
            if sum1==target:
                result.append(sub.copy())
                return 
            if val>=len(nums) or sum1 > target:
                return 
            sub.append(nums[val])
            transverse(val,sum1+nums[val])
            sub.pop()
            transverse(val+1,sum1)
        transverse(0,0)
        return result



            
            


            
        