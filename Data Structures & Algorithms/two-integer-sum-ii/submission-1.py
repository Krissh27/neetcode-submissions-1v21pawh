class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            sum1=numbers[l]+numbers[r]
            if sum1>target:
                r=r-1
            if sum1<target:
                l=l+1
            if sum1==target:
                break
        return[l+1,r+1]
        

        