class Solution:
    def confusingNumber(self, n: int) -> bool:
        num2rotated = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        
        rotated = ''
        for num in str(n)[::-1]:
            if num in num2rotated:
                rotated += num2rotated[num]
            else:
                return False

        return int(rotated) != n
