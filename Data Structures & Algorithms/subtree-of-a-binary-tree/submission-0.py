# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.reason=False
        def transverse(root):
            if root==None:
                
                return
            elif root.val==subRoot.val:
                if sss(root,subRoot):
                    self.reason =True
                    return 
            transverse(root.left)
            transverse(root.right)
                

            




        def sss(root,subroot):
            if root==None and subroot==None:
                return True
            elif root==None or subroot==None:
                return False
            elif root.val!=subroot.val:
                return False
            return (sss(root.left,subroot.left) and sss(root.right,subroot.right))
        transverse(root)

        return self.reason

            



        