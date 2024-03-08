class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        N = len(s)
        if N == 0:
            return maxLen

        left = 0
        right = 1
        vocab = set()
        ch2id = {}
        vocab.add(s[left])
        ch2id[s[left]] = left
        while left < N:
            while right < N:
                if s[right] in vocab:
                    for shift in range(left, ch2id[s[right]]+1):
                        vocab.remove(s[shift])
                    break
                else:
                    vocab.add(s[right])
                    ch2id[s[right]] = right
                    right += 1
            maxLen = max(maxLen, right - left)
            if right < N:
                left = ch2id[s[right]]
            left += 1
        return maxLen
