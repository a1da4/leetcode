class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sumdigit2num = {}
        for num in nums:
            sumdigit = sum([int(ch) for ch in str(num)])
            
            if sumdigit not in sumdigit2num:
                sumdigit2num[sumdigit] = []
            heapq.heappush(sumdigit2num[sumdigit], -num)

        answer = -1
        for heap in sumdigit2num.values():
            if len(heap) == 1:
                continue
            curr = -heapq.heappop(heap) 
            curr -= heapq.heappop(heap)

            answer = max(answer, curr)
        
        return answer

