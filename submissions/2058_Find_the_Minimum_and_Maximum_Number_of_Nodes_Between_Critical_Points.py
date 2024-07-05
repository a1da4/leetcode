# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_points = []

        def is_critical(prev_val: Union[int, None], 
                        curr_val: int, 
                        next_val: Union[int, None],
            ) -> bool:
            if prev_val is None or next_val is None:
                return False
            return prev_val > curr_val < next_val or prev_val < curr_val > next_val

        min_dist = float('inf')
        max_dist = - float('inf')
        curr_id = 0
        prev_val = None
        while head:
            curr_val = head.val
            if head.next is not None:
                next_val = head.next.val
                if is_critical(prev_val, curr_val, next_val):
                    if critical_points:
                        min_dist = min(min_dist, curr_id - critical_points[-1])
                        max_dist = max(max_dist, curr_id - critical_points[0])
                    critical_points.append(curr_id)
                prev_val = curr_val
            head = head.next
            curr_id += 1

        if len(critical_points) < 2:
            return [-1, -1]
        else:
            return [min_dist, max_dist]
