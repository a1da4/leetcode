class Solution:
    def countElements(self, arr: List[int]) -> int:
        answer = 0
        arr.sort()
        nums = set(arr)
        for num, freq in Counter(arr).items():
            if num + 1 in nums:
                answer += freq
        return answer

