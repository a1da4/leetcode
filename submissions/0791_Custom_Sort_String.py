class Solution:
    def customSortString(self, order: str, s: str) -> str:
        def sort_by_order(order, orders):
            order2char = {order_each: "" for order_each in order}
            for char in orders:
                order2char[char] += char
            return "".join([order2char[order_each] for order_each in order2char.keys()])

        orderVocab = set(order)
        orders = []
        others = []
        for char in s:
            if char in orderVocab:
                orders.append(char)
            else:
                others.append(char)
        
        orders = sort_by_order(order, orders)
        others = "".join(sorted(others))

        return orders + others
