class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        robp,robpp=0,0

        for i in range(len(nums)-2,-1,-1):
            k=max(nums[i]+robpp,robp)
            robpp=robp
            robp=k
        t1=robp
        robp,robpp=0,0
        for i in range(len(nums)-1,0,-1):
            k=max(nums[i]+robpp,robp)
            robpp=robp
            robp=k
        t2=robp

        return max(t1,t2)