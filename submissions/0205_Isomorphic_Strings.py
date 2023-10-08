class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        sVocab = set()
        tVocab = set()

        for sChar, tChar in zip(s, t):
            if sChar in sVocab:
                if s2t[sChar] != tChar:
                    return False
            else:
                if tChar in tVocab:
                    return False
                s2t[sChar] = tChar
                sVocab.add(sChar)
                tVocab.add(tChar)

        return True
