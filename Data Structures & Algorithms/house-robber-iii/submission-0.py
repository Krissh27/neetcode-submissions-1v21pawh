# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        ram=dict()
        def dfs(node):
            k=0
            if node==None:
                return 0
            if node in ram:
                return ram[node]
            k=node.val
            if node.left:
                k+=(dfs(node.left.right)+dfs(node.left.left))
            if node.right:
                k+=dfs(node.right.right)+dfs(node.right.left)
            
            ram[node]=max(k,dfs(node.right)+dfs(node.left))
            return ram[node]
        return dfs(root)


            

        