class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_a = min(prices)
        del prices[prices.index(min_a)]
        min_b = min(prices)

        if (min_a + min_b > money):
            return money
        else:
            return money - (min_a + min_b)
