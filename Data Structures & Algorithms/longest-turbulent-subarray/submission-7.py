class Solution:
    def maxTurbulenceSize(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        i=0
        if nums[i]==nums[i+1]:
            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
        if i==len(nums)-1:
            return 1


        
        maxi=2
        status=(nums[i]>nums[i+1])
        i=i+1
        count=2
        
        n=len(nums)
        while i<n-1:
            if status and nums[i]<nums[i+1]:
                status = not status
                count+=1 
            elif not status and nums[i+1]<nums[i]:
                status = not status
                count += 1
            else:
                if nums[i]==nums[i+1]:
                    while i<len(nums)-1 and nums[i]==nums[i+1]:
                        i+=1
                    if i==n-1:
                        break
                status=(nums[i]>nums[i+1])
                count=2
            maxi=max(maxi,count)
            i+=1
        return maxi

                




        