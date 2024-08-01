class Solution:
    def expand(self, s: str) -> List[str]:
        answer = [""] #TODO use heap
        N = len(s) #TODO use queue
        currId = 0
        while currId < N:
            if s[currId] == "{":
                currId += 1
                cands = []
                while s[currId] != "}":
                    if s[currId] != ",":
                        cands.append(s[currId])
                    currId += 1
            else:
                cands = [s[currId]]
            n = len(answer)
            for _ in range(n):
                ans = answer.pop(0)
                for cand in cands:
                    answer.append(ans + cand)
            
            currId += 1

        return sorted(answer)

