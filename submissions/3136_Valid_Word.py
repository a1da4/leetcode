class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        def is_number(ch: str) -> bool:
            return ord("0") <= ord(ch) <= ord("9")
        
        def is_letter(ch: str) -> bool:
            return ord("a") <= ord(ch) <= ord("z")

        def is_vowel(ch: str) -> bool:
            return ch in {"a", "e", "i", "o", "u"}

        for ch in word.lower():
            if is_number(ch):
                pass
            elif is_letter(ch):
                if is_vowel(ch):
                    has_vowel = True
                else:
                    has_consonant = True
            else:
                return False
        
        return has_vowel and has_consonant
