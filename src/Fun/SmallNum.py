arr = [100,2,4,-1,7]

min = arr[0]
for num in arr:
    if min < num:
        continue
    else:
        min = num

print(min)