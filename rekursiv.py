
__author__      = "Felix Friesenbichler"
__email__       = "1127@htl.rennweg.at"
__license__     = "GPLv2"

from time import time

def M(n):
    """
    Calculates the McCarthy-91 function.

    :param n: Starting value
    :return: McCarthy Value for n
    >>> M(101)
    91
    >>> M(99)
    91
    """
    if n <= 100:
        return M(M(n+11))
    else:
        return n - 10
