# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.rizz=True
        def transverse(root1,root2):

            if root1==None and root2==None:
                return 
            elif root1==None or root2==None:
                self.rizz=False
                return 
            elif root1.val!=root2.val:
                self.rizz=False
                return
            transverse(root1.left,root2.left)
            transverse(root1.right,root2.right)
        transverse(p,q)
        return self.rizz            

            
            


            