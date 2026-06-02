class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        res=[]
        n=len(intervals)
        while i<n and newInterval[0]>intervals[i][1]:
            
            res.append(intervals[i])
            i+=1
        ns=newInterval[0]

        ne=newInterval[1]
        while i<n and intervals[i][0]<=newInterval[1]:
            ns=min(intervals[i][0],ns)
            ne=max(ne,intervals[i][1])
            i+=1
        res.append([ns,ne])
        while i<n:
            res.append(intervals[i])
            i+=1
        return res








        