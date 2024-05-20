a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in range(len(a) // 2):
    b.append(a[i])
    b.append(a[i + len(a) // 2])

print(b)

