# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.point2val = {}

        def travel(node: Optional[TreeNode], row: int, col: int):
            if not node:
                return
            if col in self.point2val:
                self.point2val[col].append((row, node.val))
            else:
                self.point2val[col] = [(row, node.val)]
            travel(node.left, row + 1, col - 1)
            travel(node.right, row + 1, col + 1)

        travel(root, 0, 0)

        answer = []
        for col in sorted(self.point2val.keys()):
            list_row_vals = self.point2val[col]
            #print('col:', col)
            #print(' - sort (w/o key):', sorted(list_row_vals))
            #print(' - sort (w/ key):', sorted(list_row_vals, key=lambda x:x[0]))
            answer.append([row_val[1] for row_val in sorted(list_row_vals, key=lambda x:x[0])])
        return answer

