class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        numDays = len(temperatures)
        answer = [0] * numDays
        stack = []
        for currDay in range(numDays):
            if not stack or temperatures[currDay] <= stack[-1][0]:
                stack.append((temperatures[currDay], currDay))
                continue

            while stack and temperatures[currDay] > stack[-1][0]:
                temp, day = stack.pop()
                answer[day] = abs(currDay - day)
            
            stack.append((temperatures[currDay], currDay))
        return answer
