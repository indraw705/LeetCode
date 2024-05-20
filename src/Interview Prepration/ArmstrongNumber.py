
num_1= 153
a = str(num_1)
total = 0
lenthOfA = len(a)
for _ in range(lenthOfA):
    total = total + int(a[_]) ** lenthOfA

if total == num_1:
    print("its ARMSTRONG")
else:
    print("NO")