class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        candidates.sort()
        answer = []


        def travel(target: int, currId: int, path: List[int]):
            
            if target == 0:
                answer.append(path)
                return
            elif target < 0:
                return
            else:
                for candId in range(currId, N):
                    if candId > currId and \
                        candidates[candId] == candidates[candId - 1]:
                        continue
                    travel(target - candidates[candId],
                           candId + 1, path + [candidates[candId]])
        
        travel(target, 0, [])
        return answer

