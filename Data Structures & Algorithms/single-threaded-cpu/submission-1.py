class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        kk=[]
        heapq.heapify(kk)
        for i in range(len(tasks)):
            kkjj=tasks[i]
            kkjj.append(i)

            heapq.heappush(kk,kkjj)

        arr=[]
        heapq.heapify(arr)
        time=0
        res=[]

        while kk or arr:
            if  kk and (time<kk[0][0] and not arr) :
            
                time=kk[0][0]
            while kk and time>=kk[0][0]:
                zz=heapq.heappop(kk)
                
                zzz=[zz[1],zz]
                heapq.heappush(arr,zzz)
            if arr:
                kh=heapq.heappop(arr)
                res.append(kh[1][2])
                time+=kh[1][1]
        return res







        