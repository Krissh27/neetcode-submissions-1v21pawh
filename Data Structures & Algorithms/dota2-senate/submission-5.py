class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R=deque([])
        D=deque([])
        
        n=len(senate)
        for i in range(len(senate)):
            if senate[i]=='R':
                R.append(i)
            else:
                D.append(i)  


        while R and D:
            rr=R.popleft()
            dd=D.popleft()
            if rr<dd:
                R.append(rr+n)
            else:
                D.append(dd+n)  
        if R:
             return "Radiant"
        return 'Dire'


