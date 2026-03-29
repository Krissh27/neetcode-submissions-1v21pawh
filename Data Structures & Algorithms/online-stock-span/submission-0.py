class StockSpanner:

    def __init__(self):
        self.stack=[]
        

    def next(self, price: int) -> int:
        count = 0
        
        while self.stack and self.stack[-1][0] <= price:
            count += 1 + self.stack[-1][1]
            self.stack.pop()
            
        self.stack.append([price, count])
        return count + 1
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)