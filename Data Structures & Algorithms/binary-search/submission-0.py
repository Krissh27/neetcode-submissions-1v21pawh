class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        mid=(r+l)//2
        while r>=l:
            if nums[mid]>target:
                r=mid-1
               
            elif nums[mid]<target:
                l=mid+1
            elif nums[mid]==target:
                return mid
            mid=(r+l)//2 
        return -1



        