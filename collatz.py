from typing import List, Tuple

__author__ = "Felix Friesenbichler"
__email__ = "1127@htl.rennweg.at"
__license__ = "GPLv2"

def collatz(n: int) -> int:
    """
    Computes the next number in the collatz sequence.

    :param n: The current number in the sequence.
    :return: The next number in the collatz sequence.
    >>> collatz(6)
    3
    >>> collatz(7)
    22
    """

    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def collatz_sequence(number:int) -> List[int]:
    """
    Calculates the collatz sequence beginning with number.

    :param number: The beginning number for the sequence.
    :return: A list containing the calculated sequence.

    >>> collatz_sequence(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_sequence(20)
    [20, 10, 5, 16, 8, 4, 2, 1]
    """
    if number == 1:
        return [1]

    if number % 2 == 0:
        next_number = number // 2
    else:
        next_number = 3 * number + 1

    return [number] + collatz_sequence(next_number)


def longest_collatz_sequence(n: int) -> Tuple[int, int]:
    """
    Finds the longest collatz sequence starting with n

    :param n: The cap for the starting value of the collatz sequence
    :return: Starting value and length of the longest collatz sequence beginning with n
    >>> longest_collatz_sequence(100)
    (97, 119)
    >>> longest_collatz_sequence(20)
    (18, 21)
    """

    max_length = 0
    start_number = 0

    for i in range(1, n+1):
        length = len(collatz_sequence(i))
        if length > max_length:
            max_length = length
            start_number = i

    return (start_number, max_length)
