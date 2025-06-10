class Solution:
    def clearStars(self, s: str) -> str:
        answer = ""

        chs = [ch for ch in s]
        removed = set()
        ch2ids = defaultdict(list)
        for i, ch in enumerate(chs):
            if ch == "*":
                if len(ch2ids) == 0:
                    return ""
                minCh = min(ch2ids.keys())
                maxId = ch2ids[minCh].pop()
                if len(ch2ids[minCh]) == 0:
                    del ch2ids[minCh]
                removed.add(i)
                removed.add(maxId)
            else:
                ch2ids[ch].append(i)

        for i, ch in enumerate(chs):
            if i in removed:
                continue
            answer += ch

        return answer

