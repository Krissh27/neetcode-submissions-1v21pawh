class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        count=0
        result=[]
        k=[]
        kk=len(nums)
        ss=set()
        def transverse(count):
            if count==kk:
                result.append(k.copy())
            for i in nums:
                if i in ss:
                    continue
                ss.add(i)
                k.append(i)
                count+=1
                transverse(count)
                count-=1
                ss.remove(i)
                k.pop()
        transverse(count)
        return result


            
            
        
        
        
        