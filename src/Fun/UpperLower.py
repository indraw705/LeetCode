str1 = "Hello guys I'm From India, Kolhapur"

lower = 0
upper = 0

for char in str1:
    if char.islower():
        lower = lower + 1
    elif char.isupper():
        upper = upper + 1
print(f"lower : {lower} and upper : {upper}")
