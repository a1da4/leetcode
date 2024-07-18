# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        def isLeaf(node: TreeNode) -> bool:
            return not node.left and not node.right

        def travel(node: TreeNode, distance: int):
            curr = [0] * 12
            if node is None:
                return curr
            elif isLeaf(node):
                curr[0] = 1
                return curr
            else:
                left = travel(node.left, distance)
                right = travel(node.right, distance)
                
                for i in range(10):
                    curr[i + 1] += left[i] + right[i]
                curr[11] = left[11] + right[11]
            
                for d1 in range(distance + 1):
                    for d2 in range(distance + 1):
                        if 2 + d1 + d2 <= distance:
                            curr[11] += left[d1] * right[d2]
                
                return curr

        return travel(root, distance)[11]

