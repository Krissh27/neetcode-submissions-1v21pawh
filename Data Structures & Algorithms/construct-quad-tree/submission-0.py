"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n=len(grid)
        def dfs(br,bc,n):
            if n==1:
                return Node(grid[br][bc],True)
            ul=dfs(br,bc,n//2)
            ur=dfs(br,bc+n//2,n//2)
            ll=dfs(br+n//2,bc,n//2)
            lr=dfs(br+n//2,bc+n//2,n//2)
            if ul.val==ur.val==ll.val==lr.val and ll.isLeaf==True and lr.isLeaf==True and ur.isLeaf==True and ul.isLeaf==True:
                nn=Node(ll.val,True)
                return nn
            nn=Node(lr.val,False,ul,ur,ll,lr)
            return nn
        return dfs(0,0,n)
        
        


            
        