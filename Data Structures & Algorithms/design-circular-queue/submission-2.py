class MyCircularQueue:

    def __init__(self, k: int):
        self.arr=[]
        for i in range(k):
            self.arr.append(0)

        self.k=k
        self.in1=-1
        self.out=0
        self.lent=0
        

    def enQueue(self, value: int) -> bool:
        if self.lent<self.k:
            self.lent+=1
            self.in1+=1
            self.in1=self.in1%self.k
            self.arr[self.in1]=value
            
            
            return True
            

        return False

        

    def deQueue(self) -> bool:
        if self.lent<1:
            return False
        self.out+=1
        self.out=self.out%self.k
        self.lent-=1
        return True
        
        

    def Front(self) -> int:
        if not self.isEmpty():
            return self.arr[self.out]
        return -1
        

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.arr[self.in1]
        return -1
        

    def isEmpty(self) -> bool:
        if self.lent==0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.k==self.lent:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()