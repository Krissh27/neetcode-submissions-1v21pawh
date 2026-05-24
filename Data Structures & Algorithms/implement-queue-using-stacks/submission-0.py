class MyQueue:

    def __init__(self):
        self.arr=[]
        self.count=0
        self.p=0
        

    def push(self, x: int) -> None:
        self.count+=1
        self.arr.append(x)
   

    def pop(self) -> int:
        if self.count==0:
            return 
        k=self.arr[self.p]
        self.p+=1
        self.count-=1
        return k
        

    def peek(self) -> int:
       
        return self.arr[self.p]
        
        

    def empty(self) -> bool:
        if self.count==0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()