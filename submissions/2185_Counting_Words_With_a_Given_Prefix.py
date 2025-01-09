class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        answer = 0
        L = len(pref)
        for word in words:
            if len(word) < L:
                continue
            if word[:L] == pref:
                answer += 1
        return answer
