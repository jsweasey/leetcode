class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        mult = 1
        if x < 0:
            x = abs(x)
            mult = -1
        while x > 0:
            r *= 10
            r += x % 10
            x //= 10
        return r*mult if -(2**31)-1 < r*mult < 2**31 else 0

S = Solution()
print(S.reverse(-2332323))
