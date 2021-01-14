"""
# Advent of code 2020
# Day 1
# https://adventofcode.com/2020/day/1
"""
# Vim search and replace to transform data
# :%s/\n/, /g

REPORT = [
    1786, 571, 1689, 1853, 1817, 1549, 1079, 1755, 1973, 1453, 1139, 1576,
    1928, 1634, 1961, 1995, 1272, 1839, 1976, 1664, 1956, 1933, 1981, 1665,
    1057, 1798, 1485, 2004, 1990, 2002, 82, 1922, 1544, 201, 1730, 1607, 1597,
    1098, 1490, 1955, 1194, 1733, 1245, 1761, 1709, 1143, 1828, 1450, 1569,
    1997, 1943, 1555, 1958, 1176, 1858, 1937, 1560, 1979, 1962, 1658, 1959,
    2007, 1636, 1460, 348, 1084, 1952, 1162, 1772, 701, 1462, 1680, 1639, 1625,
    1060, 1600, 1631, 1638, 1350, 1675, 1366, 1244, 1413, 994, 1533, 1199,
    1653, 1902, 1340, 1819, 1676, 1081, 1953, 1993, 1652, 1214, 1815, 1977,
    1939, 2000, 1879, 1948, 1982, 1983, 1247, 1969, 1149, 1682, 1456, 2001,
    1674, 1531, 1464, 1243, 1511, 1867, 1479, 1873, 1136, 1087, 1651, 1855,
    1122, 1505, 1974, 1692, 1992, 1361, 1666, 1100, 1193, 1978, 1529, 1903,
    1510, 1152, 1514, 1591, 1753, 1744, 1985, 1459, 1954, 1579, 1307, 1975,
    1934, 1589, 971, 1603, 1980, 1942, 1160, 1986, 1963, 1921, 1481, 1736,
    1616, 1968, 1201, 1489, 1781, 1021, 1452, 1570, 1326, 1831, 2006, 1541,
    1690, 1877, 1447, 1988, 1411, 1535, 1799, 1587, 1255, 1611, 1419, 1947,
    1626, 132, 1946, 1950, 1487, 1496, 1949, 1155, 1628, 1738, 2010, 1446,
    1466, 1630, 1784, 1989, 1458, 1741
]

TEST = [1721, 979, 366, 299, 675, 1456]

####################################################
#                  PART ONE                        #
####################################################


def part_one():
    """Part 1 solution"""
    for x in REPORT:
        for y in REPORT:
            if x + y == 2020:
                mult = x * y
                # print(f'{x} x {y} = {mult}')
    print(f'Solution 1: {mult}')


part_one()

####################################################
#                  PART TWO                        #
####################################################


def part_two():
    """Part 2 solution"""
    for x in REPORT:
        for y in REPORT:
            for z in REPORT:
                if x + y + z == 2020:
                    mult = x * y * z
                    # print(f'{x} x {y} x {z} = {mult}')
    print(f'Solution 2: {mult}')


part_two()
