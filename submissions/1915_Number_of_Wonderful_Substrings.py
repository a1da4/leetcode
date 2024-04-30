class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask2freq = [0] * 1024
        mask2freq[0] += 1
        answer = 0
        mask = 0

        for c in word:
            mask ^= (1 << (ord(c) - ord('a')))
            answer += mask2freq[mask]
            for i in range(ord('j') - ord('a') + 1):
                answer += mask2freq[mask ^ (1 << i)]
            mask2freq[mask] += 1

        return answer

