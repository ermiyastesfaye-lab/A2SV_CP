class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.power(x, -n)
        else:
            return self.power(x, n)
    
    def power(self, x, n):
        if n == 0:
            return 1
        half_pow = self.power(x, n // 2)
        if n % 2 == 0:
            return half_pow * half_pow
        else:
            return half_pow * half_pow * x
