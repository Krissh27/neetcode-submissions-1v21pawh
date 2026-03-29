class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        set1={}
        for i in range(len(nums)):
            if nums[i] in set1 and abs(set1[nums[i]]-i)<=k:
                return True
               
            else:
                set1[nums[i]]=i
        return False
        