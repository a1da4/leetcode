class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer = "" 
        refLength = len(s)
        tarLength = len(t)
        if refLength < tarLength:
            return answer

        def checkCounters(refCounter, tarCounter) -> bool:
            for tar_key, tar_val in tarCounter.items():
                if tar_key not in refCounter:
                    return False
                if refCounter[tar_key] < tar_val:
                    return False
            return True

        leftId = 0
        rightId = 0
        tarCounter = Counter(t)
        refCounter = Counter(s[leftId:rightId])
        minLength = float('inf')

        while rightId < refLength:
            refCounter[s[rightId]] += 1
            rightId += 1

            while checkCounters(refCounter, tarCounter):
                if rightId - leftId < minLength:
                    minLength = rightId - leftId
                    answer = s[leftId:rightId]

                refCounter[s[leftId]] -= 1
                leftId += 1

        return answer
