class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        n=len(heights)
        pse=[-1]*n
        nge=[]
        maxi=0
        
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                stack.pop()
            if stack:
                pse[i]=stack[-1]
            stack.append(i)
            while nge and heights[i]<heights[nge[-1]]:
                k=nge.pop()
                maxi=max(maxi,(i-pse[k]-1)*heights[k])
            nge.append(i)
        while nge:
            k=nge.pop()
            maxi=max(maxi,(n-pse[k]-1)*heights[k])
        return maxi
    



        