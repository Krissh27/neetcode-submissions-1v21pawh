class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxheap)
        res=""
        while maxheap:
            m=heapq.heappop(maxheap)
            n,k=m[0],m[1]
            if res and res[-1]==k:
                if not maxheap:
                    return ""
                mm=heapq.heappop(maxheap)
                n,k=mm[0],mm[1]
                res+=k
                heapq.heappush(maxheap,m)
                if (n+1)==0:
                    continue
                heapq.heappush(maxheap,[n+1,k])
                continue
            res+=k
            if (n+1)==0:
                    continue
            heapq.heappush(maxheap,[n+1,k])
        return res
            





        