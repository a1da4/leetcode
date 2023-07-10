from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word2count1 = Counter(word1)
        word2count2 = Counter(word2)

        if set(word2count1.keys()) != set(word2count2.keys()):
            return False
        
        freqs1 = list(word2count1.values())
        freqs2 = list(word2count2.values())
        for freq in freqs1:
            if freq in freqs2:
                freqs2.remove(freq)
            else:
                return False
        
        return True
