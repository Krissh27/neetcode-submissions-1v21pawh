class FreqStack:

    def __init__(self):
        self.dis={}
        self.maxi=0
        self.count={}
        

    def push(self, val: int) -> None:
        if val not in self.count:
            self.count[val]=0
        self.count[val]+=1
        self.maxi=max(self.maxi,self.count[val])
        if self.count[val] not in self.dis:
            self.dis[self.count[val]]=[]
        self.dis[self.count[val]].append(val)
    def pop(self) -> int:
        
        k=self.dis[self.maxi].pop()
        self.count[k]-=1
        if len(self.dis[self.maxi])==0:
            self.dis.pop(self.maxi)
            self.maxi-=1
        return k
        
                
        

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()