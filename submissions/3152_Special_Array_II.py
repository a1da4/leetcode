class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        bools = []
        curr = 0
        for i, num in enumerate(nums):
            if i % 2:
                num += 1
            curr += num % 2
            bools.append(curr)

        answer = []
        for query in queries:
            left = bools[query[0] - 1] if query[0] > 0 else 0 
            if (bools[query[1]] - left) % (query[1] - query[0] + 1):
                answer.append(False)
            else:
                answer.append(True)
        
        return answer

