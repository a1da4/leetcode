# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        answer = 0
        queue = deque([root])
        while queue:
            N = len(queue)
            vals = []
            for _ in range(N):
                node = queue.popleft()
                vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            sortedVals = sorted(vals)
            for i in range(len(vals)):
                if vals[i] != sortedVals[i]:
                    answer += 1
                    sortedId = vals.index(sortedVals[i])
                    vals[i], vals[sortedId] = vals[sortedId], vals[i]

        return answer

