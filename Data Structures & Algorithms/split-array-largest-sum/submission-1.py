class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        ans=0
        
        while l<r:
            count=1
            mid=l+(r-l)//2
            zz=0
            for i in nums:
                if zz+i>mid:
                    count+=1
                    zz=0
                zz+=i
                
            if count>k:
            
                l=mid+1
            else:
                r=mid
        return l

            
        