# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        queue = deque([root])

        while queue:
            n = len(queue)
            _sum = 0
            for _ in range(n):
                node = queue.popleft()
                _sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sums.append(_sum)
        
        sums.sort(reverse=True)
        if len(sums) < k:
            return -1
        else:
            return sums[k - 1]
