# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hm={}
        for i in range(len(inorder)):
            hm[inorder[i]]=i
       
        def dfs(l,r):
            nonlocal c
            if l>r:
                return None
            nn=TreeNode(preorder[c])
            c=c+1
            nn.left=dfs(l,hm[nn.val]-1)
            nn.right=dfs(hm[nn.val]+1,r)
            return nn
        c=0
        return dfs(0,len(preorder)-1)
            
            
        