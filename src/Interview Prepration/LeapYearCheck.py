def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage
user_year = int(input("Enter a year: "))
if check_leap_year(user_year):
    print("Leap Year")
else:
    print("Not a Leap Year")