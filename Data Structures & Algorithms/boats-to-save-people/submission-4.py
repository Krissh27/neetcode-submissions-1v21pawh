class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        listn=[0]*(limit+1)
        for i in people:
            listn[i]+=1
        l=0
        r=len(listn)-1
        oo=0
        while l<=r:
            while  r>=l and listn[r]==0:
                r=r-1
            
            remains=limit-r
            if listn[r]!=0:
                oo+=1

            listn[r]-=1
            
            while l<=r and listn[l]==0:
                l=l+1
            
            if l<=r and (remains-l)>=0 :
                
                listn[l]-=1
            
            
            
           
            
                
        return oo


            

