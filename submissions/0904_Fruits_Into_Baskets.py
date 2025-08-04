class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        answer = 0
        num2freq = {}
        leftId = 0
        for currId, fruit in enumerate(fruits):
            if fruit in num2freq:
                num2freq[fruit] += 1
            else:
                num2freq[fruit] = 1
                while len(num2freq) > 2:
                    num2freq[fruits[leftId]] -= 1
                    if num2freq[fruits[leftId]] == 0:
                        del num2freq[fruits[leftId]]
                    leftId += 1
            answer = max(answer, currId - leftId + 1)

        return answer

