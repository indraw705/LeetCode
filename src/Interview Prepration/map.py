from functools import reduce

sqr = lambda x: x ** 2
lessThan250 = lambda x: x < 250
squares = list(map(sqr, [10, 11, 12, 5, 10, 18, 90, 1, 67, 2, 6, 14]))
nums = list(filter(lessThan250, squares))
print(nums)
sum_of_all = reduce(lambda x, y: x + y, nums)
print(sum_of_all)
