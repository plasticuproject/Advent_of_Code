# Advent of code 2019
# Day 4
# https://adventofcode.com/2019/day/4

####################################################
#                  PART ONE                        #
####################################################
# Find password number range


def remove_decrease(space, copy):

    # removes all passwords with decreasing numbers from left to right
    l = len(space[-1])
    for i in space:
        for j in range(l):
            try:
                if int(i[j+1]) < int(i[j]):
                    copy.remove(i)
                    break
            except (ValueError, IndexError):
                break


def check_double(copy, newSpace):

    # removes all passwords that don't have a double number in them
    l = len(copy[-1])
    for i in copy:
        for j in range(l):
            try:
                if i[j] == i[j+1]:
                    newSpace.append(i)
                    break
            except (ValueError, IndexError):
                break


def part_one(space):

    # prints number of passwords that meet the criteria of
    # functions 'remove_decrease' and 'check_double'
    print('[*] Solving...')
    copy = space.copy()
    newSpace = []
    remove_decrease(space, copy)
    check_double(copy, newSpace)
    print('CHALLENGE 1 SOLUTION: {}'.format(len(newSpace)))


# password is in this range
space = [str(i) for i in range(172851, 675870)]

# Solve challenge part 1
try:
    part_one(space)
except KeyboardInterrupt:
    quit()


####################################################
#                  PART TWO                        #
####################################################
# Build a crossed wire locator


