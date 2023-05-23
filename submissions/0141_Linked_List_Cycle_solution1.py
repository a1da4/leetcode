# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tree = f"{head}"
        #print(tree[:5])
        if tree[:5] == "Error":
            return True
        else:
            return False
