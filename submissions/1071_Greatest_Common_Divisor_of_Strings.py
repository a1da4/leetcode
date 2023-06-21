class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            x = str1
            y = str2
            srcLength = len(str1)
            tgtLength = len(str2)
        else:
            x = str2
            y = str1
            srcLength = len(str2)
            tgtLength = len(str1)
        
        for i in range(srcLength):
            rightId = srcLength - i
            if srcLength % len(x[:rightId]) > 0 or tgtLength % len(x[:rightId]):
                continue
            srcTimes = srcLength // len(x[:rightId])
            tgtTimes = tgtLength // len(x[:rightId])
            if x[:rightId] * srcTimes == x and x[:rightId] * tgtTimes == y:
                return x[:rightId]

        return ""
