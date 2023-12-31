class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxLength = -1
        char2id = {}
        chars = set()
        for charId, char in enumerate(s):
            if char in char2id:
                maxLength = max(maxLength, charId - char2id[char] - 1)
            else:
                char2id[char] = charId
                chars.add(char)

        return maxLength
