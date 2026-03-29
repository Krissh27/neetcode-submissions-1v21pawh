class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l,r=0,len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l=l+1
            r=r-1
        l,r=0,k%len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l=l+1
            r=r-1
        l,r=k%len(nums),len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l=l+1
            r=r-1




