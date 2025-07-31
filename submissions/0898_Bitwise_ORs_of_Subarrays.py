class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        curr = set()
        for num in arr:
            next = {num | _num for _num in curr}
            next.add(num)
            result.update(next)
            curr = next

        return len(result)

