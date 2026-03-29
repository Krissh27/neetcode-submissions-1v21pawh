class MinStack:

    def __init__(self):
        self.list1=[]
        

    def push(self, val: int) -> None:
        self.list1.append(val)
        

    def pop(self) -> None:
        self.list1.pop()
        

    def top(self) -> int:
        return self.list1[-1]
        

    def getMin(self) -> int:
        j=self.list1[0]
        for i in self.list1:
            if i<j:
                j=i
        return j

        
