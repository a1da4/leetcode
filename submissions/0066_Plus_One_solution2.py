class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def add(digits, currId):
            if currId < 0:
                digits.insert(0, 1)
                return digits
            else:
                if digits[currId] + 1 == 10:
                    digits[currId] = 0
                    return add(digits, currId - 1)
                else:
                    digits[currId] += 1
                    return digits

        return add(digits, len(digits) - 1)
