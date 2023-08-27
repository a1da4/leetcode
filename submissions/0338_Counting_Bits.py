class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = [0]
        for i in range(n):
            currNum = i + 1
            numBits = bin(currNum).count("1")
            answer.append(numBits)

        return answer
