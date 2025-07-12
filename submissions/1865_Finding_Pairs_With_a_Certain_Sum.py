class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.num2freq1 = Counter(nums1)
        self.num2freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        before = self.nums2[index]
        after = before + val

        self.nums2[index] += val

        self.num2freq2[before] -= 1
        self.num2freq2[after] += 1

    def count(self, tot: int) -> int:
        numPairs = 0
        for num1, freq1 in self.num2freq1.items():
            freq2 = self.num2freq2[tot - num1]
            if freq2 > 0:
                numPairs += freq1 * freq2

        return numPairs


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
