class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)
        domNum, domFreq = Counter(nums).most_common(1)[0]
        print(domNum, domFreq)
        leftFreq = 0
        for i in range(N - 1):
            leftFreq += 1 if nums[i] == domNum else 0
            rightFreq = domFreq - leftFreq

            if leftFreq > (i + 1) // 2 and rightFreq > (N - i - 1) // 2:
                return i

        return -1
