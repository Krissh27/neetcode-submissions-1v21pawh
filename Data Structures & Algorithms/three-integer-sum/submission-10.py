class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                
                
                
                if nums[i]+nums[l]+nums[r]==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l-1]==nums[l] and l<r:
                        l+=1
                    

                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    r-=1
        return res

                


        