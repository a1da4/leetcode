class Solution:
    def punishmentNumber(self, n: int) -> int:

        def isPunishment(string_num: str, target: int) -> bool:
            if not string_num and target == 0:
                return True
            if target < 0:
                return False
            for i in range(len(string_num)):
                left_string_num = string_num[:i + 1]
                right_string_num = string_num[i + 1:]
                left = int(left_string_num)

                if isPunishment(right_string_num, target - left):
                    return True

            return False

        answer = 0
        for i in range(1, n + 1):
            square = i * i
            if isPunishment(str(square), i):
                answer += square
        
        return answer

