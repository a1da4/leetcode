class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)
        answer = []
        vocabA, vocabB = set(), set()
        for i in range(N):
            vocabA.add(A[i])
            vocabB.add(B[i])
            answer.append(len(vocabA & vocabB))

        return answer
