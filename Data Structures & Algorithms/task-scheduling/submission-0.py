class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time=0
        queue=deque()
        while queue or maxHeap:
            time+=1
            if queue:
                while queue and time>=queue[0][1]:
                    j=queue.popleft()  
                    heapq.heappush(maxHeap,j[0])         

            if maxHeap:
                k=heapq.heappop(maxHeap)
                if k+1==0:
                    continue
                queue.append([k+1,time+n+1])
        return time

            



        