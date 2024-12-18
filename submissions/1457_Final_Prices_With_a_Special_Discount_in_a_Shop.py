class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        N = len(prices)
        answer = [price for price in prices]
        stack = deque([])
        for i in range(N):
            while stack and prices[stack[-1]] >= prices[i]:
                answer[stack.pop()] -= prices[i]
            stack.append(i)

        return answer

