class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        currentLength = 0
        for char in s[:k]:
            if char in "aiueo":
                currentLength += 1
        maxLength = currentLength

        for i in range(len(s) - k):
            if s[i] in "aiueo":
                currentLength -= 1
            if s[i+k] in "aiueo":
                currentLength += 1
            
            maxLength = max(currentLength, maxLength)
        
        return maxLength
