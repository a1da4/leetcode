# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        INF = float("inf")
        def search(node: Optional[TreeNode]) -> Tuple[Union[int, float],
                                                      Union[int, float],
                                                      int]:
            if not node:
                return (INF, -INF, 0)

            leftMin, leftMax, leftCount = search(node.left)
            rightMin, rightMax, rightCount = search(node.right)
            if leftMax < node.val < rightMin:
                return (min(leftMin, node.val),
                        max(rightMax, node.val),
                        leftCount + rightCount + 1)

            return (-INF, INF, max(leftCount, rightCount))

        _, _, answer = search(root)
        return answer

