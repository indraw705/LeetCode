def feb(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n :
        nex_term = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(nex_term)
    return fib_seq

print(feb(10))
print(feb(15))
print(feb(20))
