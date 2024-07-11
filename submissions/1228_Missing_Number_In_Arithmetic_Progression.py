class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diffs = [arr_j - arr_i for arr_i, arr_j in zip(arr[:-1], arr[1:])]

        if len(diffs) == 2:
            majority = diffs[0] if abs(diffs[0]) < abs(diffs[1]) else diffs[1]
        else:
            diff2freq = Counter(diffs)
            majority = diff2freq.most_common(1)[0][0]
        if majority == 0:
            return arr[0]

        for curr, diff in zip(arr[:-1], diffs):
            if diff != majority:
                return curr + majority
