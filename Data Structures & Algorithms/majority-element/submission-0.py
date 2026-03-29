class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxnum=nums[0]
        freq=1
        for i in range(1,len(nums)):
            if freq==0:
                maxnum=nums[i]
            if nums[i]==maxnum:
                freq+=1
            else:
                freq=freq-1
        return maxnum

        