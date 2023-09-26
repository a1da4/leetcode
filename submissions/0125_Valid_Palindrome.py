class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [char for char in s.lower() if char in "abcdefghijklmnopqrtsuvwxyz0123456789"]

        numChars = len(chars)
        if numChars == 0:
            return True
        
        for leftId in range(numChars//2):
            rightId = numChars - 1 - leftId
            if chars[leftId] != chars[rightId]:
                return False

        return True
