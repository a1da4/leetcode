class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        minCoins = [amount + 1 for _ in range(amount + 1)] 
        minCoins[0] = 0

        for currentAmount in range(amount + 1):
            for coin in coins:
                if coin <= currentAmount:   
                    minCoins[currentAmount] = min(minCoins[currentAmount], minCoins[currentAmount - coin] + 1)
        
        if minCoins[amount] == amount + 1:
            return -1
        
        return minCoins[amount]
