class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _temp, _day = stack.pop()
                answer[_day] = abs(day - _day)
            
            stack.append((temp, day))
        return answer
