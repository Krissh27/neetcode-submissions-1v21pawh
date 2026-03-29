class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=-float('inf')
        maxi2=0
        for i in nums:
            maxi2+=i
            maxi=max(maxi,maxi2)
            if maxi2<0:
                maxi2=0
                continue
            
        
        return maxi
            


        