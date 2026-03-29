class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        sub=[]
        def transverse(val):
            if len(sub)==k:
                result.append(sub.copy())
                return 
            if val>n:
                return
            sub.append(val)
            transverse(val+1)
            sub.pop()
            transverse(val+1)
        transverse(1)
        return result


            

        