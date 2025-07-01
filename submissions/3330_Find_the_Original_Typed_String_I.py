class Solution:
    def possibleStringCount(self, word: str) -> int:
        answer = 1
        freq = 1
        curr = word[0]

        for ch in word[1:]:
            if curr == ch:
                freq += 1
            else:
                if freq > 1:
                    answer += freq - 1
                freq = 1
                curr = ch

        return answer + (freq - 1)
