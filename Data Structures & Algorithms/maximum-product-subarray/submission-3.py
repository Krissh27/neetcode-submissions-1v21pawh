class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        
        cmax=1
        cmin=1
        res=-float('inf')

        for i in nums:
            temp=cmax
            cmax=max(cmax*i,cmin*i,i)
            cmin=min(temp*i,i,cmin*i)
            res=max(res,cmax)
        return res
        
            
           
        