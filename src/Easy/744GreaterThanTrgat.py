# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        max = 0
        final = letters[0]
        for letter in letters:
            if letter == target:
                continue
            elif ord(letter) < ord(target):
                continue
            else:
                if max < (ord(letter) - ord(target)):
                    max = (ord(letter) - ord(target))
                    final = letter
            return final

        return letters[0]


obj = Solution()
print(obj.nextGreatestLetter(["c", "f", "j"], "a"))
print(obj.nextGreatestLetter(["c", "f", "j"], "c"))
print(obj.nextGreatestLetter(["x", "x", "y", "y"], "z"))
print(obj.nextGreatestLetter(["k", "a", "q"], "m"))
print(obj.nextGreatestLetter(["k", "a", "q"], "r"))
