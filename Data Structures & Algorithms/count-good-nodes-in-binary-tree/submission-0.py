# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        mvalue=float('-inf')
        self.count=0
        
        def transverse(root,mvalue):
            if root ==None:
                return 
            if root.val>=mvalue:
                mvalue=root.val
                self.count+=1
            transverse(root.left,mvalue)
            transverse(root.right,mvalue)
            return self.count
        return transverse(root,mvalue)

            




        