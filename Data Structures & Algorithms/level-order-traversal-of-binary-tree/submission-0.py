# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=deque([root])
        result=[]
        while queue:
            ql=len(queue)
            k=[]
            for i in range(ql):
               
                z=queue.popleft()
                k.append(z.val)
                if z.left != None:
                    queue.append(z.left)
                if z.right !=None:
                    queue.append(z.right)
            result.append(k)
        
        return result



        