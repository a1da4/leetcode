# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]

        x, y = 0, 0
        dirId = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()

        if head:
            matrix[0][0] = head.val
            visited.add((0, 0))
            head = head.next

        while head:
            dx, dy = directions[dirId]

            if (x + dx, y + dy) in visited or \
               x + dx < 0 or x + dx >= m or \
               y + dy < 0 or y + dy >= n:

                dirId = (dirId + 1) % 4
                continue
            
            x += dx
            y += dy
            visited.add((x, y))
            matrix[x][y] = head.val
            head = head.next

        return matrix

