class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        curr = k % sum(chalk)
        left, right = 0, len(chalk) - 1

        while left < right:
            mid = (left + right) // 2
            if sum(chalk[:mid + 1]) <= curr:
                left = mid + 1
            else:
                right = mid 
        
        return left

