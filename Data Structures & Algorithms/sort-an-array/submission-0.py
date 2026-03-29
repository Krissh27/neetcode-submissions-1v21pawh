class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l,r):
            i,j=0,0
            nl=[]
            while i<len(l) and j<len(r):
                if l[i]>=r[j]:
                    nl.append(r[j])
                    j=j+1
                elif l[i]<r[j]:
                    nl.append(l[i])
                    i=i+1
            nl.extend(l[i:])
            nl.extend(r[j:])
            return nl

        def dis(nums: List[int]) -> List[int]:
            if len(nums)<2:
                return nums
            mid=len(nums)//2
            l=dis(nums[:mid])
            r= dis(nums[mid:])
            return merge(l,r)
        return dis(nums)
        



        