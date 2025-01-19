
__author__      = "Felix Friesenbichler"
__email__       = "1127@htl.rennweg.at"
__license__     = "GPLv2"

def is_palindrom(s: str):
    """
    This method checks if the string s, which contains only one word, is a
    palindrome.

    >>> is_palindrom("racecar")
    True

    >>> is_palindrom("string")
    False
    """

    first_list = list(s)
    second_list = list(s)
    second_list.reverse()

    if first_list == second_list:
        return True
    else:
        return False
