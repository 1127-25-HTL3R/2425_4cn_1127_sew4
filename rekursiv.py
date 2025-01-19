
__author__      = "Felix Friesenbichler"
__email__       = "1127@htl.rennweg.at"
__license__     = "GPLv2"

from time import time

def M(n):
    """
    Calculates the McCarthy-91 function.

    :param n: Starting value
    :return: McCarthy Value for n
    >>> M(99)
    91
    >>> M(150)
    140
    """
    if n <= 100:
        return M(M(n+11))
    else:
        return n - 10

if __name__ == "__main__":
    t0 = time()
    m_list = [M(n) for n in range(200)]
    m_dict = {n: M(n) for n in range(200)}
    t1 = time()
    print(f"Time: {t1-t0:.6f} Seconds")

    # Bemerkungen:
    # Für n < 100 gibt M(n) immer 91 zurück.
    # Für n > 100 gibt M(n) immer n - 10.
    # Es dauert 0.000611 Sekunden zum ausführen
