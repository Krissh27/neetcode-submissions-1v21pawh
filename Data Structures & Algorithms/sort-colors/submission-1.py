class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l,m=0,0
        r=len(nums)-1
        while m<=r:
            if nums[m]==1:
                m=m+1
            elif nums[m]==0:
                nums[m],nums[l]=nums[l],nums[m]
                l=l+1
                m=m+1
            else:
                nums[r],nums[m]=nums[m],nums[r]
                r=r-1
        