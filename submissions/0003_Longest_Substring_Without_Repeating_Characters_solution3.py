class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        N = len(s)
        if N == 0:
            return maxLen

        left, right = 0, 1
        vocab = set(s[left])
        ch2id = {s[left]: left}
        while left < N:
            while right < N:
                ch = s[right]
                if ch in vocab:
                    for shift in range(left, ch2id[ch]+1):
                        vocab.remove(s[shift])
                    break
                else:
                    vocab.add(ch)
                    ch2id[ch] = right
                    right += 1
            maxLen = max(maxLen, right - left)
            if right < N:
                left = ch2id[ch]
            left += 1
        return maxLen
