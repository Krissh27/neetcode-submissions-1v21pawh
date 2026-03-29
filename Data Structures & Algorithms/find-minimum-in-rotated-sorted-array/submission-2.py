class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        mid=(l+r)//2
        res=float("inf")
        
        while l<=r:
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                res=min(res,nums[mid])
                r=mid-1
            mid=(l+r)//2

        return res
           

            
