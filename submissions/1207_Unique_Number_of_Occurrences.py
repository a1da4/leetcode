from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        char2freq = Counter(arr)
        freqVocab = set()
        for freq in char2freq.values():
            if freq in freqVocab:
                return False
            else:
                freqVocab.add(freq)

        return True
