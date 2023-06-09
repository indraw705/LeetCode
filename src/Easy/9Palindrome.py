# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        :param x: integer
        :return: true if its palindrome
        """
        return str(x) == str(x)[::-1]


obj=Solution()
print(obj.isPalindrome(1212))
print(obj.isPalindrome(1212345654321))
print(obj.isPalindrome(98789))
print(obj.isPalindrome(12387))
print(obj.isPalindrome(56765))