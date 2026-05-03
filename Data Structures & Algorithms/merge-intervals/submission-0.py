class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        n=len(intervals)
        i=0
        res=[]
        temp=intervals[0]
        for s, e in intervals:
            if s<=temp[1]:
                temp[1]=max(temp[1],e)
            else:
                res.append(temp)
                temp=[s,e]
        res.append(temp)
        return res

        