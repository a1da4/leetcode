class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        chs = [str(num) for num in nums]
        chs.sort(key=lambda ch: ch * 10, reverse=True)

        if chs[0] == "0":
            return "0"

        return ''.join(chs)

