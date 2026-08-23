class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        sumi=sum(nums)
        mini=0
        maxmini=float('inf')
        maxi=0
        maxmaxi=-float('inf')
        for i in nums:
            mini+=i
            
            if mini>0:
                mini=0
            maxi = max(i, maxi + i) 
            maxmini=min(maxmini,mini)
            maxmaxi=max(maxmaxi,maxi)
        if maxmaxi<0:
            return maxmaxi
        return max(sumi-maxmini,maxmaxi)
        