class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        C1 = Counter(word1)
        C2 = Counter(word2)
        
        C2_keys = set(C2.keys())
        C2_vals = list(C2.values())

        for word, freq in C1.items():
            if word in C2_keys:
                if freq in C2_vals:
                    C2_vals.remove(freq)
                else:
                    return False
            else:
                return False
        return True
