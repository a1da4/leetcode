class Solution:
    def update(self, answerEach: List[int], candidates: List[int], target: int) -> None:
        candidateTail = answerEach[-1]
        candidateSum = sum(answerEach)
        for candidate in candidates:
            if candidate < candidateTail:
                continue
            tempSum = candidateSum + candidate
            if tempSum == target:
                tempList = []
                tempList.extend(answerEach)
                tempList.append(candidate)
                self._answer.append(tempList)
            if tempSum < target:
                tempList = []
                tempList.extend(answerEach)
                tempList.append(candidate)
                self.update(tempList, candidates, target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self._answer: List[List[int]] = []
        for candidate in candidates:
            if candidate == target:
                self._answer.append([candidate])
                continue
            self.update([candidate], candidates, target)
        
        return self._answer
