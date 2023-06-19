# https://leetcode.com/problems/plus-one/description/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''.join(str(i) for i in digits)
        # a = int(a)+1
        return [int(i) for i in str(int(a)+1)]


obj = Solution()
print(obj.plusOne([1,2,3]))
print(obj.plusOne([4,3,2,1]))
print(obj.plusOne([9]))