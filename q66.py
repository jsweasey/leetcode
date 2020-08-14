from typing import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits)-1] += 1
        if digits[len(digits)-1] > 9:
            for x in range(len(digits), -1, -1):
                if digits[x-1]>9:
                    if x == 1:
                        digits[x-1] = 0
                        digits.insert(0,1)
                    else:
                        digits[x-1] = 0
                        digits[x-2] += 1
        return digits

S = Solution()
print(S.plusOne([1,9,8,9]))
