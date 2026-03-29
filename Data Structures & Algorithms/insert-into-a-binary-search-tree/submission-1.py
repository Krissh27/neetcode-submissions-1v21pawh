# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node=TreeNode(val)
        if root is None:
            root=new_node
            return root
        rizz=root
        temp=None
        while rizz!=None:
            temp=rizz
            if rizz.val>val:
                rizz=rizz.left
            else:
                rizz=rizz.right
        if temp.val>val:
            temp.left=new_node
        else:
            temp.right=new_node
        return root

        