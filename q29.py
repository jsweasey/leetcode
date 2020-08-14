from typing import *

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n = i = m = div = 0
        sign = [1,-1][divisor < 0 or dividend < 0]
        sign = [sign,1][divisor < 0 and dividend < 0]
        while True:
            if n > abs(dividend):
                i -= m
                n -= div
                while True:
                    if n > abs(dividend):
                        i -= 1
                        break
                    n += abs(divisor)
                    i +=1
                break
            m += 1
            div += abs(divisor)
            n += div
            i += m
        return sign*i #if -(2**31)-1 < sign*i < (2**31)-1 else (2**31)-1

S = Solution()
print(S.divide(21465757483454545648, 4675))
