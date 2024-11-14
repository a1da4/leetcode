class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 0, max(quantities)

        def verify(x: int) -> bool:
            currId = 0
            quantity = quantities[currId]

            for i in range(n):
                if quantity <= x:
                    currId += 1
                    if currId == len(quantities):
                        return True
                    else:
                        quantity = quantities[currId]
                else:
                    quantity -= x

            return False

        while left < right:
            mid = (left + right) // 2
            if verify(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

