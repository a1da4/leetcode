class Solution:
    def maxTotalFruits(
        self, 
        fruits: List[List[int]], 
        startPos: int, 
        k: int,
    ) -> int:
        pos2fruit = {pos: fruit for pos, fruit in fruits}
        initPoint = pos2fruit.get(startPos, 0)

        leftPoints = [0] * (k + 1)
        rightPoints = [0] * (k + 1)

        leftPos, rightPos = startPos, startPos
        leftFruits, rightFruits = 0, 0

        for i in range(1, k + 1):
            leftPos -= 1
            rightPos += 1

            leftFruits += pos2fruit.get(leftPos, 0)
            rightFruits += pos2fruit.get(rightPos, 0)

            leftPoints[i] += leftFruits
            rightPoints[i] += rightFruits

        answer = max(
            initPoint + leftPoints[k],
            initPoint + rightPoints[k], 
        )
        for i in range(1, k):
            rest = k - 2 * i
            if rest <= 0:
                continue
            answer = max(
                answer,
                initPoint + leftPoints[i] + rightPoints[rest],
                initPoint + rightPoints[i] + leftPoints[rest],
            )

        return answer

