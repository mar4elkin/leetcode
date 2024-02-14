class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
        half_power = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half_power * half_power
        else:
            return x * half_power * half_power
