class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)
        if ns == nt == 0:
            return False
        elif abs(ns - nt) >= 2:
            return False
        else:
            if ns != nt:
                if ns == nt + 1:
                    s, t = t, s
                    ns, nt = nt, ns

                if s == "":
                    return True

                for currId in range(ns):
                    if s[currId] != t[currId]:
                        return s[currId:] == t[currId+1:]
                
                return True
                
            else:
                if s == t:
                    return False

                diff = 0
                for sChar, tChar in zip(s, t):
                    if sChar != tChar:
                        diff += 1
                        if diff > 1:
                            return False
                
                return True
