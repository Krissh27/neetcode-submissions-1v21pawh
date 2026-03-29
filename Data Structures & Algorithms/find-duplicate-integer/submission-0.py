class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f,s=0,0
        s=nums[s]
        f=nums[nums[f]]
        while nums[s]!=nums[f]:
            s=nums[s]
            f=nums[nums[f]]
        f=0
        while nums[s]!=nums[f]:
            s=nums[s]
            f=nums[f]
        return nums[f]


        