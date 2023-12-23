class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()
        N = len(candidates)
        for startNumId in range(N):
            currCand = candidates[startNumId]
            if currCand > target:
                break
            if currCand == target:
                answer.append([currCand])
            candSums = [([currCand], currCand)]
            while candSums:
                M = len(candSums)
                for _ in range(M):
                    currCands, currSum = candSums.pop(0)
                    for numId in range(startNumId, N):
                        cand = candidates[numId]
                        if currCands[-1] > cand:
                            continue
                        if currSum + cand == target:
                            answer.append(currCands + [cand])
                        if currSum + cand < target:
                            candSums.append((currCands + [cand], currSum + cand))
                    
        return answer
