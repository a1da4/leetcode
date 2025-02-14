import math
class ProductOfNumbers:

    def __init__(self):
        self.prods = []
        self.n = 0

    def add(self, num: int) -> None:
        if self.n > 0:
            if num > 1:
                for i in range(self.n):
                    self.prods[i] *= num
            elif num == 0:
                self.prods = [0] * self.n
            else:
                pass        
        self.prods.append(num)        
        self.n += 1

    def getProduct(self, k: int) -> int:
        return self.prods[-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
