class MedianFinder:

    def __init__(self):
        self.count=0
        self.minright=[]
        self.maxleft=[]

    def addNum(self, num: int) -> None:
        self.count+=1
        if self.maxleft and num<=-self.maxleft[0]:
            heapq.heappush(self.maxleft,-num)
        else:
            heapq.heappush(self.minright,num)



        if len(self.minright)+1<len(self.maxleft):
            k=heapq.heappop(self.maxleft)
            heapq.heappush(self.minright,-k)
        elif len(self.minright)>len(self.maxleft)+1:
            k=heapq.heappop(self.minright)
            heapq.heappush(self.maxleft,-k)   
        

    def findMedian(self) -> float:
        if self.count%2==1:
            if len(self.minright)>len(self.maxleft):
                return self.minright[0]
            else:
                return -self.maxleft[0]
        else:
            return (self.minright[0]-self.maxleft[0])/2



        
        