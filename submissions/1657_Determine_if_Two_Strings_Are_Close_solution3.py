class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        C1 = Counter(word1)
        C2 = Counter(word2)

        return Counter(C1.values()) == Counter(C2.values())
