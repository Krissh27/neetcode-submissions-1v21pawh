class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dict1={}
        count=0
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1 
        result=[]
        k=[]
        def transverse(count):
            if count==len(nums):
                result.append(k.copy())
                return
            for i in dict1:
                if dict1[i]>0:
                    dict1[i]-=1
                    k.append(i)
                    transverse(count+1)
                    k.pop()
                    dict1[i]+=1
        transverse(count)
        return result








        