
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


def is_palindrome_sentence(s: str):
    """
    Checks is the string s, which may contain a sentence, is a
    palindrome
    sentence.

    >>> is_palindrome_sentence("Was it a car or a cat I saw?")
    True

    >>> is_palindrome_sentence("Do Geese see God?")
    True

    >>> is_palindrome_sentence("A Toyota")
    True

    >>> is_palindrome_sentence("Warsaw was raw")
    True
    """

    char_list = (" ", ";", "?", ".", ",", ":", "!")
    string = s.lower()

    for char in char_list:
        string = string.replace(char, "")

    return is_palindrom(string)
