class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        numCoins = [amount + 1] * (amount + 1)
        numCoins[0] = 0
        for currAmount in range(amount + 1):
            for coin in coins:
                if currAmount >= coin:
                    numCoins[currAmount] = min(numCoins[currAmount], numCoins[currAmount - coin] + 1)

        target = numCoins[amount]
        if target == amount + 1:
            return -1
        else:
            return numCoins[amount]
