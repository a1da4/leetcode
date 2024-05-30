class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        answer = 0
        left = None
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if left is None:
                    left = 0
                    for _i in range(i, j):
                        left ^= arr[_i]
                else:
                    left ^= arr[j - 1]
                right = arr[j]
                for k in range(j, len(arr)):
                    if j < k:
                        right ^= arr[k]
                    if left == right:
                        answer += 1
            left = None
        return answer

