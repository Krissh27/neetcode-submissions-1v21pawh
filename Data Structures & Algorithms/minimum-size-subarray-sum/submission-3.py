class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r,k=0,0,nums[0]
        count=10000000
        while l<len(nums):
            if k<target and (r+1)<len(nums):
                r=r+1
                k=k+nums[r]
            elif k>=target:
                count=min(r-l+1,count)
                k=k-nums[l]
                l=l+1
            else:
                break
                
                
        if count==10000000:
            return 0
        return count
                
            