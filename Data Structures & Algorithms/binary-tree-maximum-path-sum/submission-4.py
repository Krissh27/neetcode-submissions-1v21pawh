# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=-float("inf")
        def dfs(node):
            nonlocal maxi
            if node==None:
                return 0
            
            r=dfs(node.right)
            l=dfs(node.left)
            maxi=max(maxi,(r+l+node.val),max(r,l)+node.val,node.val)
            return max(max(r,l)+node.val,node.val)
        dfs(root)
        return maxi


        