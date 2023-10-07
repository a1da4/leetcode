class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)
        for key, val in ransomCounter.items():
            if key not in magazineCounter:
                return False
            if magazineCounter[key] < val:
                return False
        
        return True
