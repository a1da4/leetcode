class Solution:
    def distributeCandies(
        self, 
        n: int, 
        limit: int,
    ) -> int:
        answer = 0
        for i in range(min(limit, n) + 1):
            left = max(0, n - i - limit)
            right = min(limit, n - i) + 1
            if left >= right:
                continue
            answer += right - left

        return answer

