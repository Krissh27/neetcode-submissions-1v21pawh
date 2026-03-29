# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.count=0
        def transverse(root):
            if root==None:
                return 0
            left=transverse(root.left)
            right=transverse(root.right)
            self.count=max((left+right),self.count)
            return (max(left,right)+1)
        transverse(root)
        return self.count
        
        