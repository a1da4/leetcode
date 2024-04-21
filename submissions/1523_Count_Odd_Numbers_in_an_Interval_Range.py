class Solution:
    def countOdds(self, low: int, high: int) -> int:
        answer = (high - low) // 2 + high % 2 + low % 2
        if high%2 and low%2:
            return answer - 1
        else:
            return answer
