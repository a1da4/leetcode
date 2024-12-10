class Solution:
    def maximumLength(self, s: str) -> int:
        def _count(s: str, curr: str) -> int:
            n = len(curr)
            return sum([s[i:i+n] == curr for i in range(0, len(s) - n + 1)])

        ch2freq = Counter(s)
        answer = 0
        for ch, freq in ch2freq.items():
            if freq > 2:
                curr = ch * (freq - 1)
                num = _count(s, curr)
                while curr and num < 3:
                    curr = curr[:-1]
                    num = _count(s, curr)
                answer = max(answer, len(curr))

        return answer if answer > 0 else -1

