class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        m = '0'
        i=1
        def binary(m,k,i):
            if i == n:
                return m[k-1]
            inverted_m = ''.join('1' if digit == '0' else '0' for digit in m)
            m = m+'1' + inverted_m[::-1]
            i+=1
            return binary(m,k,i)
        return binary(m,k,i)
