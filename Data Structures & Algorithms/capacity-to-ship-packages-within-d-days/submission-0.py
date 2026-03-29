class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        w=(l+r)//2
        sample=0
        res=r
        while l<=r:
            ships=1
            k=w
            
            for i in weights:
                
                
                if k-i<0:
                    ships+=1
                    k=w
                k-=i
            if ships>days:
                sample=False
            else:
                sample=True





            if sample==True:
                res=min(res,w)
                r=w-1
            else:
                l=w+1
            w=(l+r)//2
        return res



            
                    
        