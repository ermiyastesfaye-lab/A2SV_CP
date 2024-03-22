class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.list(x)
        rev = lst[::-1]
        if (lst == rev):
            return True
        else:
            return False


    def list(self, n):
        global lst
        lst = []
        string = str(n)
        for m in string:
            lst.append(m)
        return lst
