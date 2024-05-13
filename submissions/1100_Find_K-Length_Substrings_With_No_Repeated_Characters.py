class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        ch2freq = Counter(s[:k])
        answer = 1 if len(ch2freq) == k else 0
        for currId in range(len(s) - k):
            ch2freq[s[currId]] -= 1
            if ch2freq[s[currId]] == 0:
                del ch2freq[s[currId]]
            ch2freq[s[currId + k]] += 1
            if len(ch2freq) == k:
                answer += 1

        return answer

