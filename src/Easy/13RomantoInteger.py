# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        letters = s[::-1]
        total = 0
        compareVal = values.get(letters[0])
        for letter in letters:
            if compareVal <= values.get(letter):
                total = total + values.get(letter)
                compareVal = values.get(letter)
            elif compareVal > values.get(letter):
                total = total - values.get(letter)
        return total

    # Solution2
    #  roman_to_integer = {
    #         'I': 1,
    #         'V': 5,
    #         'X': 10,
    #         'L': 50,
    #         'C': 100,
    #         'D': 500,
    #         'M': 1000,
    #     }
    #     s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
    #     return sum(map(lambda x: roman_to_integer[x], s))






obj = Solution()
print(obj.romanToInt("III"))  # 3
print(obj.romanToInt("LVIII"))   # 58
print(obj.romanToInt("MCMXCIV"))   #1994
print(obj.romanToInt("DCCV"))   #705
print(obj.romanToInt("MCCCXII"))  #1312
print(obj.romanToInt("MCCV"))