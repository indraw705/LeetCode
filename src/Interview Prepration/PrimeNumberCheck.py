
def checkPrimeNum(num):
    if num == 1:
        return False
    else:
        for i in range(2, int((num * 0.5)+1)):
            if num % i == 0:
                return False
            else:
                return True


print(checkPrimeNum(1))
print(checkPrimeNum(12))
print(checkPrimeNum(13))
print(checkPrimeNum(17))
print(checkPrimeNum(18))