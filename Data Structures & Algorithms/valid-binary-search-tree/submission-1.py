# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def transverse(node,l,r):
            if node==None:
                return True
            if node.val>l and node.val<r:
                return transverse(node.left,l,node.val) and transverse(node.right,node.val,r)
            else:
                return False
        return transverse(root,float('-inf'),float('inf'))

