# Vim search and replace to transfrom data
# :%s/\n/, /g

RATES = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]


def part_one():
    r = RATES.copy()
    r.sort()
    r.insert(0, 0)
    r.append(r[len(r) - 1] + 3)
    ones = []
    threes = []
    for i, ele in enumerate(r[:-1]):
        if r[i + 1] - ele == 1:
            ones.append(ele)
        if r[i + 1] - ele == 3:
            threes.append(ele)
    result = len(ones) * len(threes)
    return result

x = part_one()
print(x)
