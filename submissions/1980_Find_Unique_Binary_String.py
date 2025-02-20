class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums[0]) # num of bit

        vocab = set(nums)
        items = []

        def travel(curr: str):
            if len(curr) == N:
                items.append(curr)
            elif len(curr) < N:
                for bit in ["0", "1"]:
                    travel(curr + bit)
            else:
                pass

        travel("")

        for item in items:
            if item not in vocab:
                return item
