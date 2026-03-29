# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list1=[]
        def transversal(root):
            if root==None:
                return list1
            transversal(root.left)
            
            transversal(root.right)
            list1.append(root.val)
            return list1
        return transversal(root)
        