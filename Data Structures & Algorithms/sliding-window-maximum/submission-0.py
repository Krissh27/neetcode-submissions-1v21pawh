class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res=[]
        for i in range(k-1):
            if not q:
                q.append([nums[i],i])
                continue
            while q and q[-1][0]<nums[i]:
                q.pop()
            q.append([nums[i],i])



        for i in range(k-1,len(nums)):

            
            while q and q[-1][0]<nums[i]:
                q.pop()
            q.append([nums[i],i])
            if i-q[0][1]==k:
                q.popleft()
            res.append(q[0][0])
        return res





        