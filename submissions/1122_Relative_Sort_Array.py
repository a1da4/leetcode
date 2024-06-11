class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]: 
        num2freq = Counter(arr1)

        answer = []
        for num in arr2:
            if num2freq[num] > 0:
                answer += [num] * num2freq[num]
                num2freq[num] = 0

        for num in sorted(num2freq.keys()):
            if num2freq[num] > 0:
                answer += [num] * num2freq[num]
                num2freq[num] = 0

        return answer

