class BIT:
    def __init__(self, size: int):
        self.N = size + 2
        self.tree = [0] * self.N

    def update(self, i: int, x: int):
        i += 1
        while i < self.N:
            self.tree[i] += x
            i += i & -i

    def query(self, i: int):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def query_range(self, l: int, r: int):
        return self.query(r) - self.query(l - 1)

class Solution:
    def goodTriplets(
        self, 
        nums1: List[int], 
        nums2: List[int],
    ) -> int:
        answer = 0
        N = len(nums1)

        """ O(N^3)
        for i in range(N):
            for j in range(i + 1, N):
                if nums2.index(nums1[i]) >= nums2.index(nums1[j]):
                    continue
                for k in range(j + 1, N):
                    if nums2.index(nums1[j]) < nums2.index(nums1[k]):
                        answer += 1
        """

        """ O(N^2)
        num2pos = {num: pos for pos, num in enumerate(nums2)}
        mapped = [num2pos[num] for num in nums1]

        for j in range(N):
            left = 0
            for i in range(j):
                if mapped[i] < mapped[j]:
                    left += 1

            right = 0
            for k in range(j + 1, N): 
                if mapped[j] < mapped[k]:
                    right += 1
            
            answer += left * right
        """

        # O(NlogN)
        num2pos = {num: pos for pos, num in enumerate(nums2)}
        mapped = [num2pos[num] for num in nums1]

        bit = BIT(N)
        left = [0] * N
        for i, val in enumerate(mapped):
            left[i] = bit.query(val - 1)
            bit.update(val, 1)
        
        bit = BIT(N)
        right = [0] * N
        for i in reversed(range(N)):
            val = mapped[i]
            right[i] = bit.query_range(val + 1, N - 1)
            bit.update(val, 1)

        answer += sum(l * r for l, r in zip(left, right))

        return answer

