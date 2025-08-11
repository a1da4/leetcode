class Solution:
    def productQueries(
        self,
        n: int,
        queries: List[List[int]],
    ) -> List[int]:
        binN = bin(n)[2:]
        powers = []
        for digit, binary in enumerate(binN[::-1]):
            if binary == '0': continue
            powers.append(int(binary) * 2 ** digit)

        mod = 10 ** 9 + 7
        cumPowers = [powers[0]]
        cumPower = powers[0]
        for power in powers[1:]:
            cumPower = cumPower * power
            cumPowers.append(cumPower)

        answers = []
        for left, right in queries:
            excluded = 1 if left == 0 else cumPowers[left - 1]
            answers.append(
                (cumPowers[right] // excluded) % mod
            )

        return answers

