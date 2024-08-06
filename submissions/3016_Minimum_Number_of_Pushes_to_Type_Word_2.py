class Solution:
    def minimumPushes(self, word: str) -> int:
        answer = 0
        for i, item in enumerate(Counter(word).most_common()):
            ch, freq = item
            answer += (i // 8 + 1) * freq

        return answer

