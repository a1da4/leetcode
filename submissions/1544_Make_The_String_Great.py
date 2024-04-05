class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 1:
            return s
        prev = ""
        curr = s
        while prev != curr:
            prev = curr
            curr = ""
            currId = 0
            while currId < len(s):
                if currId == len(s) - 1:
                    curr += s[currId]
                elif s[currId] != s[currId + 1] \
                        and s[currId].lower() == s[currId + 1].lower():
                    currId += 1
                else:
                    curr += s[currId]
                currId += 1

            s = curr
        
        return curr

