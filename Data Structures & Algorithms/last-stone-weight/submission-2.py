class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        self.maxh=[]
        for i in stones:
            heapq.heappush(self.maxh,-i)
        while len(self.maxh)>1:
            k=-heapq.heappop(self.maxh)
            m=-heapq.heappop(self.maxh)
            
            if k>m:
                t=m-k
                heapq.heappush(self.maxh,t)
        if len(self.maxh)==0:
            return 0
        return -self.maxh[0]
            

        