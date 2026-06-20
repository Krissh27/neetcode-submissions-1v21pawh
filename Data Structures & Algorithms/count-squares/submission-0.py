class CountSquares:

    def __init__(self):
        self.h=defaultdict(int)
        self.points=[]
        

    def add(self, point: List[int]) -> None:
        self.points.append((point[0],point[1]))
        if (point[0],point[1]) not in self.h:
            self.h[(point[0],point[1])]=0
        self.h[(point[0],point[1])]+=1
        

    def count(self, point: List[int]) -> int:
        px,py=point
        seen=set()
        res=0
        for x, y in self.points:
            if (abs(py - y) != abs(px - x)) or x == px or y == py or (x,y) in seen :

                continue
            
            res+=self.h[(x,y)]*self.h[(px,y)]*self.h[(x,py)]
            seen.add((x,y))
        return res


        
