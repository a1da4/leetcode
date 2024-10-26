# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.node2depth: Dict[int, int] = {}
        self.node2height: Dict[int, int] = {}

    def _calcDepth(self, node: Optional[TreeNode], depth: int = 0) -> int:
        if not node:
            return 0
        self.node2depth[node.val] = depth
        lHeight = self._calcDepth(node.left, depth + 1)
        rHeight = self._calcDepth(node.right, depth + 1)
        height = max(lHeight, rHeight) + 1
        self.node2height[node.val] = height

        return height
    
    def _delQuery(self, query: int) -> int:
        qDepth = self.node2depth[query]
        heights = self.depth2height[qDepth]
        if len(heights) == 1:
            return qDepth - 1
        else:
            if self.node2height[query] == heights[0]:
                return qDepth + heights[1] - 1
            return qDepth + heights[0] - 1

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self._calcDepth(root)
        self.depth2height = defaultdict(list)
        for node, height in self.node2height.items():
            self.depth2height[self.node2depth[node]].append(height)

        for heights in self.depth2height.values():
            heights.sort(reverse=True)
        
        answer = []
        for query in queries:
            answer.append(self._delQuery(query))

        return answer

