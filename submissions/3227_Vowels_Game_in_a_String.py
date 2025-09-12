class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u"}
        numVowels = 0
        for ch in s:
            if ch in vowels:
                numVowels += 1
        
        return numVowels > 0
