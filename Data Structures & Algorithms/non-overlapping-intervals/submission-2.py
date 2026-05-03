class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        output=[]
        res=[]
        count=0
        for s,e in intervals:
            if len(output)==0:
                output.append([s,e])
                continue
            if s<output[-1][1]:
                count+=1
            else:
                output.append([s,e])
        return count

        



        