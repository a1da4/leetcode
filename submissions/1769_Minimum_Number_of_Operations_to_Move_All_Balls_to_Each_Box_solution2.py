class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        answer = [0] * N

        prevLeft = 0
        opsFromLeft = 0
        for i in range(N):
            answer[i] += opsFromLeft
            prevLeft += int(boxes[i])
            opsFromLeft += prevLeft

        prevRight = 0
        opsFromRight = 0
        for i in range(N - 1, -1, -1):
            answer[i] += opsFromRight
            prevRight += int(boxes[i])
            opsFromRight += prevRight

        return answer

