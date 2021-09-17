'''
for a given list with size N return a list filled with distances to all '0' in it
at least one '0' is guaranteed

complexity:
    time: O(N)
    space: O(N)

example:
    input
        5
        0 1 4 9 0
    output
        0 1 2 1 0
'''


import sys


def compute_distances(n: list):
    res = list()
    first_zero = n.index('0')

    # filling left part
    distance = first_zero
    for i in range(first_zero+1):
        res.append(distance)
        distance -= 1

    # main part
    offset = first_zero + 1
    cont = True
    while cont:
        try:
            zero_idx = n.index('0', offset)
            # one element list
            if zero_idx == 0:
                res.append(0)
                offset = zero_idx + 1
                continue
            delta = zero_idx - offset
            distance = 1
            mid = int(delta / 2)
            for i in range(mid):
                res.append(distance)
                distance += 1

            if delta % 2 == 0:
                distance -= 1

            l2 = delta - mid + 1
            for i in range(l2):
                res.append(distance)
                distance -= 1
            offset = zero_idx + 1
        except ValueError:
            cont = False

    # filling right part
    distance = 1
    for i in range(len(n) - offset):
        res.append(distance)
        distance += 1
    return res


def find_distance_to_zeros():
    # size of list
    n = int(sys.stdin.readline().rstrip())
    # list of elements (with at least one '0')
    street = sys.stdin.readline().rstrip().split(' ')

    result = compute_distances(street)
    print(*result)
    #return *result


if __name__ == '__main__':
    find_distance_to_zeros()
