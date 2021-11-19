#a)
cubes_list = []
cubes_list_17 = []
all_sum = 0
for i in range(1, 1000, 2):
    cubes_list.append(i ** 3)
for ind, val in enumerate(cubes_list):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += cubes_list[ind]
print(all_sum)
#b)
for m in cubes_list:
    cubes_list_17.append(m + 17)
all_sum = 0
for ind, val in enumerate(cubes_list_17):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //=10
    if sum_digits % 7 == 0:
        all_sum += cubes_list_17[ind]
print(all_sum)
