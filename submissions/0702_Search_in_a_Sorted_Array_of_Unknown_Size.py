# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        INF = 2 ** 31 - 1
        left, right = 0, 10 ** 4 - 1

        while left <= right:
            print(left, right)
            mid = (left + right) // 2
            val = reader.get(mid)
            if val == target:
                return mid
            elif val == INF or val > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1 

