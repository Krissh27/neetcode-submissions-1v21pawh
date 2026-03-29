# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kv=None
        self.count=0
        def transverse(root):
            if root==None:
                return 0
            transverse(root.left)
            self.count+=1
            if self.count==k:
                self.kv=root
            transverse(root.right)
            return 0
        transverse(root)
        return self.kv.val
            

            
            