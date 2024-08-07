class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", 
                "Six", "Seven", "Eight", "Nine", "Ten", 
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
                "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", 
                "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        result = ""
        thousandId = 0

        while num:
            if num % 1000 != 0:
                _result = ""
                curr = num % 1000

                if curr >= 100:
                    _result += ones[curr // 100] + " Hundred "
                    curr %= 100

                if curr >= 20:
                    _result += tens[curr // 10] + " "
                    curr %= 10

                if curr > 0:
                    _result += ones[curr] + " "

                _result += thousands[thousandId] + " "
                result = _result + result

            num //= 1000
            thousandId += 1

        return result.strip()

