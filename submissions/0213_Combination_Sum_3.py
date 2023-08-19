class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 55:
            return []
        
        answer = []
        nums = [i for i in range(1, 10)]

        cands = []
        for currNum in nums[:-k+1]:
            if currNum <= n:
                cands.append([currNum])
        
        numItems = 1
        while numItems < k and cands:
            numCands = len(cands)
            for _ in range(numCands):
                currCand: List[int] = cands.pop(0)
                currSum = sum(currCand)
                lastNum = currCand[-1]

                if numItems < k - 1:
                    currNums = nums[:-k+1+numItems]
                else:
                    currNums = nums
                for currNum in currNums:
                    if currNum <= lastNum:
                        continue
                    if currSum + currNum < n and numItems + 1 < k:
                        cands.append(currCand + [currNum])
                    elif currSum + currNum == n and numItems + 1 == k:
                        answer.append(currCand + [currNum])
                    else:
                        continue
            
            numItems += 1
    
        return answer
