# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def getVal(head: Optional[TreeNode], vals: List[int]):
            if not head:
                return None
            vals.append(head.val)
            val = getVal(head.left, vals)
            if type(val) == int(): 
                vals.append(val)
            val = getVal(head.right, vals)
            if type(val) == int():
                vals.append(val)
            return vals

        if root:
            vals = getVal(root, [])

            head = root
            head.val = vals[0]
            for val in vals[1:]:
                head.right = TreeNode(val)
                head.left = None
                head = head.right

