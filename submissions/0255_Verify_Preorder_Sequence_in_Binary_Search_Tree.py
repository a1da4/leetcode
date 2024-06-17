class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        minLim = - float('inf')
        stack = []

        for num in preorder:
            while stack and stack[-1] < num:
                minLim = stack.pop()
            
            if num <= minLim:
                return False
            
            stack.append(num)

        return True

