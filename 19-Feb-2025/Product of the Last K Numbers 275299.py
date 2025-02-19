# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.prod = 1
        self.prefix = [1]
    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = []
            self.prod = 1
        else:
            self.prod *= num
            self.prefix.append(self.prod)
            
    def getProduct(self, k: int) -> int:
        if len(self.prefix) < k:
            return 0
        if len(self.prefix) == k:
            return self.prefix[-1]
        res = self.prefix[-1] // self.prefix[-k-1]
        return res


        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)