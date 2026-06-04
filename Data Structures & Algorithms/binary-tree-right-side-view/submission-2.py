# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.count=0
        self.l=[]
        def dfs(node):
            if node==None:
                return
            self.count+=1 
            if self.count>len(self.l):
                self.l.append(node.val)
            dfs(node.right)
            dfs(node.left)
            self.count-=1 
        dfs(root)
        return self.l

            
            


        