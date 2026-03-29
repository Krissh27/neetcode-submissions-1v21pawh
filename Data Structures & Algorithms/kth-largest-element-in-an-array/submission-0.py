class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.arr=nums
        mini=[]
        
        for i in (self.arr):
            heapq.heappush(mini,i)
            if len(mini)>k:
                heapq.heappop(mini)
            
        return mini[0]
            


        