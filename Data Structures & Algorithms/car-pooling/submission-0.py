class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cap=capacity
        heap = [(x[1], x) for x in trips]
        count=[]

        heapq.heapify(heap)
        arr=[]
        while heap:
            key,ele=heapq.heappop(heap)
            while count and ele[1]>=count[0][0]:
                k=heapq.heappop(count)
                cap+=k[1][0]
            
            cap=cap-ele[0]
            new=[ele[2],ele]
            heapq.heappush(count,new)
            if cap<0:
                return False
        return True



        