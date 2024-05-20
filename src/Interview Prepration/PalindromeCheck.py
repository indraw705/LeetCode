# 1982
def palindromeCheck(num):
    return str(num) == str(num)[::-1]


print(palindromeCheck(111111))
print(palindromeCheck(123454321))
print(palindromeCheck(6789098765))
print(palindromeCheck(909090909))
print(palindromeCheck(11112))
