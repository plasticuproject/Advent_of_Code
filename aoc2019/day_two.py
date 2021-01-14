# Advent of code 2019
# Day 2
# https://adventofcode.com/2019/day/2

####################################################
#                  PART ONE                        #
####################################################
# Building an INTCODE Computer


def add_operation(codes, instruction_pointer):

    # ADD values at instruction parameter addresses
    # and store result in memory
    parameter1 = codes[instruction_pointer + 1]
    parameter2 = codes[instruction_pointer + 2]
    parameter3 = codes[instruction_pointer + 3]
    codes[parameter3] = codes[parameter1] + codes[parameter2]


def multiply_operation(codes, instruction_pointer):

    # MULTIPLY values at instruction parameter addresses
    # and store result in memory
    parameter1 = codes[instruction_pointer + 1]
    parameter2 = codes[instruction_pointer + 2]
    parameter3 = codes[instruction_pointer + 3]
    codes[parameter3] = codes[parameter1] * codes[parameter2]


def halt_operation(codes):

    # return list/memory object and halt program
    return codes


def computer(program):

    # steps though our list/memory input (program) and performs
    # operations on addresses

    # copy initial program state to new list/memory object
    codes = program.copy()

    # Read opcodes, operate, and advance instruction pointer
    instruction_pointer = 0
    while True:

        # opcode 1 = ADD
        if codes[instruction_pointer] == 1:
            add_operation(codes, instruction_pointer)
            instruction_pointer += 4

        # opcode 2 = MULTIPLY
        elif codes[instruction_pointer] == 2:
            multiply_operation(codes, instruction_pointer)
            instruction_pointer += 4

        # opcode 99 = HALT
        elif codes[instruction_pointer] == 99:
            return halt_operation(codes)

        # invalid opcode values will raise this error
        else:
            raise ValueError('Invaild program input')


def tests():

    # test 1
    test1 = [1,0,0,0,99]
    solution1 = [2,0,0,0,99]
    test_one = computer(test1)
    assert test_one == solution1, 'Failed test 1'

    # test 2
    test2 = [2,3,0,3,99]
    solution2 = [2,3,0,6,99]
    test_two = computer(test2)
    assert test_two == solution2, 'Failed test 2'

    # test 3
    test3 = [2,4,4,5,99,0]
    solution3 = [2,4,4,5,99,9801]
    test_three = computer(test3)
    assert test_three == solution3, 'Failed test 3'

    # test 4
    test4 = [1,1,1,4,99,5,6,0,99]
    solution4 = [30,1,1,4,2,5,6,0,99]
    test_four = computer(test4)
    assert test_four == solution4, 'Failed test 4'

    #test 5
    test5 = [1,9,10,3,2,3,11,0,99,30,40,50]
    solution5 = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    test_five = computer(test5)
    assert test_five == solution5, 'Failed test 5'

    # if all tests pass then return
    return 'All tests passed'


# run tests
tests()

# challenge program
program = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,1,13,23,27,1,6,27,31,
2,31,13,35,1,9,35,39,2,39,13,43,1,43,10,47,1,47,13,51,2,13,51,55,1,55,9,59,1,59,
5,63,1,6,63,67,1,13,67,71,2,71,10,75,1,6,75,79,1,79,10,83,1,5,83,87,2,10,87,91,1,
6,91,95,1,9,95,99,1,99,9,103,2,103,10,107,1,5,107,111,1,9,111,115,2,13,115,119,1,
119,10,123,1,123,10,127,2,127,10,131,1,5,131,135,1,10,135,139,1,139,2,143,1,6,
143,0,99,2,14,0,0]

# run challenge program and print solution
solution = computer(program)
print('Program output:')
print(solution)
print('\nCHALLENGE SOLUTION: {}\n'.format(solution[0]))


####################################################
#                  PART TWO                        #
####################################################
# Brute Forcing An INTCODE Program


# populate dictionary with tuples from (0,0) to (99,99)
tup_dict = {}
index_number = 0
for parameter1 in range(100):
    for parameter2 in range(100):
        tup_dict[index_number] = (parameter1, parameter2)
        index_number += 1


def substitute(tup, program):

    # function to subtitute values in memory address 1 and 2
    # (the first ADD instruction parameters)
    # run computer() and return memory address 0

    # copy initial program state to new list/memory object
    # and substitute instruction parameters with tuple values
    program2 = program.copy()
    program2[1] = tup[0]
    program2[2] = tup[1]

    try:
        # run computer with amended program
        # return value at memory address 0
        output = computer(program2)
        return output[0]

    # catch any errors
    except (ValueError, IndexError) as error:
        print(error)


# brute force the computer program until we find the 2 parameter values
# we need to create 19690720 in memory address 0
for key, tup in tup_dict.items():
        output = substitute(tup, program)

        # if/when parameter values are found print them and get the challenge
        # solution by calculating solution = 100 * location_1 + location_2
        if output == 19690720:
            print('NOUN: {0}\nVERB: {1}'.format(tup[0], tup[1]))
            print('CHALLENGE SOLUTION: {}'.format(100 * tup[0] + tup[1]))

