# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=-float('inf')
        def dfs(k):
            nonlocal maxi
            if k==None:
                return 0
            l=max(0,dfs(k.left))
            r=max(0,dfs(k.right))
            
            maxi=max(maxi,l+r+k.val)
            return k.val+max(l,r)
        dfs(root)
        return maxi
            
        