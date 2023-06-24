class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelIds = []
        s = list(s)
        for currId, currChar in enumerate(s):
            if currChar in "aiueoAIUEO":
                vowelIds.append(currId)

        for i in range(len(vowelIds)//2):
            srcId = vowelIds[i]
            tgtId = vowelIds[-1-i]
            s[srcId], s[tgtId] = s[tgtId], s[srcId]

        return "".join(s)
