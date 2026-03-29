class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        u,l= piles[0],1
        for i in range(1,len(piles)):
            if u<piles[i]:
                u=piles[i]
            
        while l<=u:
            count=0
            mid=(l+u)//2
            for i in piles:
               count+= math.ceil(i/mid)
            if count>h:
                l=mid+1
            elif count<=h:
                u=mid-1
        return l

