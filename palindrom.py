
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


def palindrome_product(x):
    """
    Finds the biggest palindrome number (smaller than x), which is the product
    of 3 digit number

    >>> palindrome_product("String")
    Traceback (most recent call last):
        ...
    ValueError: x must be numeric

    """

    if not str(x).isdigit():
        raise ValueError("x must be numeric")


    max_pal = 1
    last_pal = 1
    for i in range(100, 999):

        for j in range(100, 999):
            heir = i * j

            if is_palindrom(str(heir)) and heir < x:
                last_pal = max_pal
                max_pal = heir


    print(max_pal)
    return max_pal
