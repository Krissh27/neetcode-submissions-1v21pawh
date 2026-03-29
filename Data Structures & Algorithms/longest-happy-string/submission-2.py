class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        last=["",0]
        arr=[[-a,"a"],[-b,"b"],[-c,"c"]]
        heapq.heapify(arr)
        kk = arr
        strr=""

        while kk:
            m=heapq.heappop(kk)
            k,n=m[0],m[1]
            if k==0:
                return strr
            if len(strr)>=2 and strr[-1]==strr[-2]==n:
                if kk:
                    mm=heapq.heappop(kk)
                else:
                    return strr
                
                k,n=mm[0],mm[1]
                if k==0:
                    return strr
                strr+=n
                heapq.heappush(kk,m)
                if k+1==0:
                    continue
                heapq.heappush(kk,[k+1,n])
                continue
                

            strr+=n
            if k+1==0:
                    continue
            heapq.heappush(kk,[k+1,n])
        return strr

            

                
                

        
        




            




        