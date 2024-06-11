# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        def _average(node: Optional[TreeNode]):
            _vals = []
            _queue = deque([node])
            while _queue:
                _N = len(_queue)
                for _ in range(_N):
                    _node = _queue.popleft()
                    _vals.append(_node.val)
                    if _node.left:
                        _queue.append(_node.left)
                    if _node.right:
                        _queue.append(_node.right)
            return sum(_vals) / len(_vals)
        
        maxAvg = 0
        queue = deque([root])
        while queue:
            N = len(queue)
            for _ in range(N):
                node = queue.popleft()
                avg = _average(node)
                maxAvg = max(maxAvg, avg)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return maxAvg

