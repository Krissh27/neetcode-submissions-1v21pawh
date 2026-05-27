class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,0
        count=0
        while r<n-1:
            k=r
            for i in range(l,k+1):
                r = max(r,i+nums[i])
            
            l=k+1
            count+=1
        return count
        
        

        