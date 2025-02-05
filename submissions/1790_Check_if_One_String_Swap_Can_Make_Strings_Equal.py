class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        pre1, pre2 = None, None
        shift = 0
        for ch1, ch2 in zip(s1, s2):
            if ch1 == ch2:
                continue
            else:
                if pre1 is None and pre2 is None:
                    pre1, pre2 = ch1, ch2
                elif shift == 0 and pre1 == ch2 and pre2 == ch1:
                    shift += 1
                    continue
                else:
                    return False
        if shift == 0 and pre1 is not None and pre2 is not None:
            return False    
        return True
        
