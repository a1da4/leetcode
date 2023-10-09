class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p2s = {}
        sVocab = set()
        pVocab = set()
        sWords = s.split()

        if len(pattern) != len(sWords):
            return False

        for p, sWord in zip(pattern, sWords):
            if p in pVocab:
                if p2s[p] != sWord:
                    return False
            else:
                if sWord in sVocab:
                    return False
                p2s[p] = sWord
                sVocab.add(sWord)
                pVocab.add(p)
        return True
