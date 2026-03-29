class TimeMap:

    def __init__(self):
        self.dict1={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict1:
            self.dict1[key].append([value,timestamp])
        else:
            self.dict1[key]=[[value,timestamp]]
       
    


        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict1:
            return ""
        l,r=0,len(self.dict1[key])-1
        res=""
        while l<=r:
            mid=l+(r-l)//2
            if self.dict1[key][mid][1]==timestamp:
                return self.dict1[key][mid][0]
            elif self.dict1[key][mid][1]<timestamp:
                res= self.dict1[key][mid][0]
                l=mid+1
            else:
                r=mid-1
        return res


        
