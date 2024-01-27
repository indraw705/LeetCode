def prime_checker(number):
    if number < 1:
        print("It's not a prime number.")
    elif number == 2:
        print("It's a prime number.")
    elif number % 2 == 0:
        print("It's not a prime number.")
    else:
        for i in range(3,int(number*0.5)+1,2):
            if number % i == 0:
                print("It's not a prime number.")
                break
            else:
                print("It's a prime number.")


prime_checker(87)