class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.minheap=[]
        for i in points:
            heapq.heappush(self.minheap,[-(i[0]**2+i[1]**2),i[0],i[1]])
            if len(self.minheap)>k:
                heapq.heappop(self.minheap)

        
        res=[]
        while self.minheap:
            d,x,y=heapq.heappop(self.minheap)
            res.append([x,y])
        return res



        

        return k

        