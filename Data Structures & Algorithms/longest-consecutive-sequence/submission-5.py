class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        max1=0
        for i in set1:
            max2=0
            nus=i
            if (nus-1) in set1:
                continue

            while nus in set1:
                max2+=1
                nus+=1
                
            if max2>max1:
                max1=max2
        return max1


            
    
