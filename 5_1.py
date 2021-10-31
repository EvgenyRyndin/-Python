def odd_nums(max_val):
    n = 1
    while n <= max_val:
        yield n
        n += 2

odd_to_15 = odd_nums(15)
3