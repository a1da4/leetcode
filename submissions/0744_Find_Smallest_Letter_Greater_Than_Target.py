class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        tarOrd = ord(target)

        while left <= right:
            mid = (left + right) // 2

            if ord(letters[mid]) > tarOrd:
                right = mid - 1
            else:
                left = mid + 1

        if left >= len(letters):
            return letters[0]
        else:
            return letters[left]

