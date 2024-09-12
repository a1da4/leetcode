class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        vocab = set(allowed)
        answer = 0

        for word in words:
            answer += 1
            for ch in word:
                if ch not in vocab:
                    answer -= 1
                    break
        return answer

