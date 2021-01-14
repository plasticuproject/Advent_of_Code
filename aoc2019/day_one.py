# Advent of code 2019
# Day 1
# https://adventofcode.com/2019/day/1

####################################################
#                  PART ONE                        #
####################################################
# Build a Fuel Counter-Upper


# test input and output
test_modules = [12,14,1969,100756]
test_solutions = [2, 2, 654, 33583]


def fuel(modules):

    # our fuel calculator
    # fuel = mass // 3 - 2
    total_fuel = 0
    count = 1
    for mass in modules:
        fuel = mass // 3 - 2
        total_fuel += fuel

        # for running with test input
        if modules == test_modules:
            assert fuel == test_solutions[count - 1], 'failed test {}'.format(c)
        count += 1

    return 'TOTAL FUEL/CHALLENGE SOLUTION: ' +  str(total_fuel)


# run test
fuel(test_modules)

# challenge modules
modules = [93326, 54591, 106194, 129163, 110634, 81294, 59548, 77988, 66354, 108990,
91097, 102076, 67526, 135820, 109167, 94391, 78323, 75009, 61836, 55751, 54229,
145159, 103821, 136601, 119830, 57607, 69157, 115099, 53756, 136063, 62243, 111594,
57598, 83789, 130669, 67435, 112187, 141492, 109872, 84640, 119694, 119030, 75716,
119017, 106547, 101674, 120137, 93759, 115976, 119378, 86245, 93317, 53712, 69079,
92125, 62397, 102365, 115860, 111618, 65452, 83625, 90951, 110774, 114943, 99559,
101417, 100651, 98412, 109963, 68158, 121405, 85002, 119519, 92200, 125104, 71018,
131892, 92342, 51671, 94691, 136330, 64877, 65449, 65008, 91656, 144705, 130867,
74732, 61977, 129490, 91928, 109200, 94488, 99216, 89115, 89756, 52113, 83463,
101765, 62363]

# run challenge program
solution = fuel(modules)
print(solution)


####################################################
#                  PART TWO                        #
####################################################
# Build a better Fuel Counter-Upper


test_modules = [12,14,1969,100756]
test_solutions = [2, 2, 966, 50346]


def fuel_two(modules):

    # our fuel calculator
    # fuel = mass // 3 - 2
    total_fuel = 0
    count = 1
    for mass in modules:
        module_fuel = 0
        fuel = mass // 3 - 2
        module_fuel += fuel

        # recursively add fuel mass and recalculate
        while fuel > 0:
            fuel = fuel // 3 - 2
            if fuel < 0:
                fuel = 0
            module_fuel += fuel
        total_fuel += module_fuel

        # for running with test input
        if modules == test_modules:
            assert module_fuel == test_solutions[count - 1], 'failed test {}'.format(c)
        count += 1

    return 'TOTAL FUEL/CHALLENGE SOLUTION: ' +  str(total_fuel)


# run test
fuel_two(test_modules)

# run challenge program
solution = fuel_two(modules)
print(solution)

