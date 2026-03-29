class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        k=0

        for i in range(n-2,-1,-1):
            k+=1
            if nums[i]>=k:
                k=0
        if k==0:
            return True
        return False
            

        