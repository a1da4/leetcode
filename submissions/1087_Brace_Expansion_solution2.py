class Solution:
    def expand(self, s: str) -> List[str]:
        answer = [""] #TODO use heap
        s = deque([ch for ch in s])
        while s:
            ch = s.popleft()
            if ch == "{":
                cands = []
                ch = s.popleft()
                while ch != "}":
                    if ch != ",":
                        cands.append(ch)
                    ch = s.popleft()
            else:
                cands = [ch]
            n = len(answer)
            for _ in range(n):
                ans = answer.pop(0)
                for cand in cands:
                    answer.append(ans + cand)

        return sorted(answer)
