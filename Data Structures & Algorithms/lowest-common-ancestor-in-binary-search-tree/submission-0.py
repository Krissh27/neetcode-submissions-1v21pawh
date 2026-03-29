# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans=None
        
        def dfs(node):
            nonlocal ans
            if node==None:
                return False
            l=dfs(node.left) 
            r=dfs(node.right)
            mid = (node.val == p.val or node.val == q.val)

            if (mid and l) or (mid and r) or (l and r):
                ans = node

            
            
            return l or r or mid
        dfs(root)
        return ans

        