class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pfs=dict()
        sumi=0
        count=0
        for i in range(len(nums)):
            if sumi in pfs:
                pfs[sumi]+=1
            else:
                pfs[sumi]=1
            sumi+=nums[i]
            if (sumi-k) in pfs:
                count+=pfs[sumi-k]
        return count

            
          

        