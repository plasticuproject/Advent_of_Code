"""
# Advent of code 2020
# Day 10
# https://adventofcode.com/2020/day/10
"""
# Vim search and replace to transfrom data
# :%s/\n/, /g

RATES = [
    35, 111, 135, 32, 150, 5, 106, 154, 41, 7, 27, 117, 109, 63, 64, 21, 138,
    98, 40, 71, 144, 13, 66, 48, 12, 55, 119, 103, 54, 78, 65, 112, 39, 128,
    53, 140, 77, 34, 28, 81, 151, 125, 85, 124, 2, 99, 131, 59, 60, 6, 94, 33,
    42, 93, 14, 141, 92, 38, 104, 9, 29, 100, 52, 19, 147, 49, 74, 70, 84, 113,
    120, 91, 97, 17, 45, 139, 90, 116, 149, 129, 87, 69, 20, 24, 148, 18, 58,
    123, 76, 118, 130, 132, 75, 110, 105, 1, 8, 86
]

TEST = [
    28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1,
    32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3
]

# RATES = TEST

####################################################
#                  PART ONE                        #
####################################################


def part_one():
    """Part 1 solution"""
    r = RATES.copy()
    r.sort()
    r.insert(0, 0)
    r.append(r[len(r) - 1] + 3)
    ones = 0
    threes = 0
    for i, ele in enumerate(r[:-1]):
        if r[i + 1] - ele == 1:
            ones += 1
        if r[i + 1] - ele == 3:
            threes += 1
    result = ones * threes
    return result


solution = part_one()
print(f'Solution 1: {solution}')

####################################################
#                  PART TWO                        #
####################################################

# WIP
"""
RATES = [1, 2, 3, 4, 5]


def part_two():
    r = RATES.copy()
    r.sort()
    r.insert(0, 0)
    r.append(r[len(r) - 1] + 3)
    count = 0
    for i, ele in enumerate(r[:-1]):
        rr = r.copy()
        print(f'i = {i}')
        c = 0
        for j in range(i + 1):
            print(f'j = {j}')
            print(rr)
            try:
                print(
                    f'{rr[j + 1 + c]} - {rr[j+ c]} = {rr[j + 1 + c] - rr[j + c]}'
                )
                input()
                if rr[j + 1 + c] - rr[j + c] <= 3:
                    del rr[j + 1 + c]
                    count += 1
                    c += 1
            except IndexError:
                break

    print(count)


part_two()
"""
