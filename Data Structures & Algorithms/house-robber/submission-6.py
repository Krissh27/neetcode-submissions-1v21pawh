class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        pp=nums[-1]
        p=nums[-2]
        for i in range(len(nums)-3,-1,-1):
            k=max(nums[i]+pp,p)
            pp=p
            p=k
        return p