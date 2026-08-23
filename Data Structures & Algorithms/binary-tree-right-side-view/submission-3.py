# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        count=0
        def dfs(node,l):
            if not node:
                return 
            nonlocal ans
            nonlocal count
            if l>=count:
                ans.append(node.val)
                count+=1
            dfs(node.right,l+1)
            dfs(node.left,l+1)
            return 
        dfs(root,0)
        return ans

            

            
            
            


        