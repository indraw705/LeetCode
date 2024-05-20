list_1 = [2, 6, 5, 7, 12, 0]
target_sum = 12




for i in range(len(list_1)):
    for j in range(len(list_1)):
        if i == j:
            continue
        elif list_1[i] + list_1[j] == target_sum:
            print(f"the indices are {i} & {j}")

