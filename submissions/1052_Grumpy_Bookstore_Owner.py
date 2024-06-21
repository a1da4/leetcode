class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        if len(customers) == minutes:
            return sum(customers)

        answer = sum([customer if grump == 0 else 0 for customer, grump \
                    in zip(customers, grumpy)])

        currCustom = sum([customer if grump else 0 for customer, grump \
                        in zip(customers[:minutes], grumpy[:minutes])])
        maxCustom = currCustom

        for currId in range(len(customers) - minutes):
            currCustom -= customers[currId] if grumpy[currId] else 0
            currCustom += customers[currId + minutes] if grumpy[currId + minutes] else 0
            maxCustom = max(maxCustom, currCustom)

        return answer + maxCustom

