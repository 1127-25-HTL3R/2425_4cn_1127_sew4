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
