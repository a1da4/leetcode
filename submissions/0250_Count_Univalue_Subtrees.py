# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        
        def is_univalue(node: Optional[TreeNode]) -> bool:
            _queue = deque([node])
            _unival = node.val
            while _queue:
                _N = len(_queue)
                for _ in range(_N):
                    _node = _queue.popleft()
                    if _node.val != _unival:
                        return False
                    if _node.left:
                        _queue.append(_node.left)
                    if _node.right:
                        _queue.append(_node.right)
            return True

        
        answer = 0
        if root:
            queue = deque([root])
            while queue:
                N = len(queue)
                for _ in range(N):
                    node = queue.popleft()
                    if is_univalue(node):
                        answer += 1
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        
        return answer

