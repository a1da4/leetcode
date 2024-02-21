class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0:
          return 0
        
        shift = 0
        while left != right:
            left = left >> 1
            right = right >> 1
        
            shift += 1

        return left << shift
