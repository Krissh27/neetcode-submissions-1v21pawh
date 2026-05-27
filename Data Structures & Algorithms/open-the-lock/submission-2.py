class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q=deque(["0000"])
        seen=set(deadends)
        lent=len(q)
        time=0
        if "0000" in seen:
            return -1
        while q:
            for _ in range(len(q)):
                k=q.popleft()
                if k==target:
                    return time
                for i in range(len(k)):
                    
                    for move in (-1,1):
                        lj=int(k[i])+move
                        lj=lj%10
                        n=k[:i]+str(lj)+k[i+1:]
                        if n in seen:
                            continue
                        seen.add(n)
                        q.append(n)
            time+=1
        return -1

        

        

        
        