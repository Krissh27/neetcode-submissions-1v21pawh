class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=1
        l=1
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                count+=1
                nums[l]=nums[i+1]
                l=l+1

        return count
        