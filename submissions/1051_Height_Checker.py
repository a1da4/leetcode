class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        answer = 0
        for height, expected in zip(heights, sorted(heights)):
            if height != expected:
                answer += 1
        
        return answer

