# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        char2alp = {char: chr(97 + char) for char in range(26)}
        nodes = [(root, "")]
        chars = []
        while nodes:
            N = len(nodes)
            for _ in range(N):
                node, curr = nodes.pop(0)
                curr += char2alp[node.val]
                if node.left is None and node.right is None:
                    chars.append(curr)
                if node.left:
                    nodes.append((node.left, curr))
                if node.right:
                    nodes.append((node.right, curr))

        smallestChar = sorted([char[::-1] for char in  chars])[0]

        return smallestChar

