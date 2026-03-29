class MinStack:

    def __init__(self):
        self.list1=[]
        self.mini=[]
        

    def push(self, val: int) -> None:
        self.list1.append(val)
        if self.mini and self.mini[-1]>=val or len(self.mini)==0:
            self.mini.append(val)
        
            
        

    def pop(self) -> None:
        j=self.list1.pop()
        if j==self.mini[-1]:
            self.mini.pop()
            if len(self.mini)==0 and len(self.list1)>0:
                self.mini.append(self.list1[-1])

        

    def top(self) -> int:
        return self.list1[-1]
        

    def getMin(self) -> int:
        return self.mini[-1]
        
