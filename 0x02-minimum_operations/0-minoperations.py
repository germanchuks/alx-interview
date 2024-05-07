#!/usr/bin/python3
"""
Method that calculates the fewest number of operations needed to result in
exactly n H characters in a file.
"""


def minOperations(n: int) -> int:
    """Returns the fewest number of operations needed to result
    in exactly n H characters in a file"""
    if (n <= 0):
        return 0

    char_list = ['H']
    operations = 0

    while (len(char_list) != n):
        char = 'H'
        if ((len(char_list) % 2 == 0 or len(char_list) == 1)
                and len(char_list) ** 2 <= n):
            char = ''.join(char_list)
            for elem in char:
                char_list.append(elem)
            operations += 2
        else:
            char_list.append(char)
            operations += 1
        # print(char_list)

    return operations
