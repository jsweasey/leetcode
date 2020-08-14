from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List = []
        for indice1 in range(len(nums)):
            for indice2 in (range((indice1+1),len(nums))):
                if (nums[indice1] + nums[indice2] == target):
                    List.append(indice1)
                    List.append(indice2)
        return List

S = Solution()
print(S.twoSum([2, 7, 11, 15], 9))
