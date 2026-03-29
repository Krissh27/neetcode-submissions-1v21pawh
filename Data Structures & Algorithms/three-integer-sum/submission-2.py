class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list1=[]
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            if i > 0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                ts = nums[i] + nums[l] + nums[r]
                if ts>0:
                    r=r-1
                elif ts<0:
                    l=l+1
                elif ts==0 and [nums[i],nums[l],nums[r]] not in list1:

                    list1.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    r=r-1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return list1


        