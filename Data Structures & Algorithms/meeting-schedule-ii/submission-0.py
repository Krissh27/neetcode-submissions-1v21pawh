"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time=0
        heap = []
        maxi=0
        
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals)):
            k=intervals[i]
            time=k.start
            while heap and heap[0]<=time:
                heapq.heappop(heap)
            heapq.heappush(heap, k.end)
            maxi=max(maxi,len(heap))
        return maxi

            


        