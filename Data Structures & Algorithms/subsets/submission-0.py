class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        sub=[]
        k=len(nums)
        def transverse(val):
            if val>=(k):
                result.append(sub.copy())
                return
            
            sub.append(nums[val])
            transverse(val+1)
            sub.pop()
            transverse(val+1)
        transverse(0)
        return result







        