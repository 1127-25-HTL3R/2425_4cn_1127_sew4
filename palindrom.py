
__author__      = "Felix Friesenbichler"
__email__       = "1127@htl.rennweg.at"
__license__     = "GPLv2"


def is_palindrome(s: str):
    """
    This method checks if the string s, which contains only one word, is a
    palindrome.

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("string")
    False
    """

    return s == s[::-1]


def is_palindrome_sentence(s: str) -> bool:
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
    nonalnum = [' ', ',', '.', '!', '?', "'", '"', '-', ':', ';']

    cleaned = ""
    for char in s:
        if char not in nonalnum:
            cleaned += char.lower()

    return cleaned == cleaned[::-1]


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

            if is_palindrome(str(heir)) and heir < x:
                last_pal = max_pal
                max_pal = heir


    print(max_pal)
    return max_pal


def to_base(number: int, base: int) -> str:
    """
    Converts a decimal number to the wished representation in another
    base.

    :param number: Zahl im 10er-System
    :param base: Zielsystem (maximal 36)
    :return: Zahl im Zielsystem als String

    >>> to_base(1234,16)
    '4D2'
    >>> to_base(10,2)
    '1010'
    """
    if base > 36 or base < 2:
        raise ValueError("Base must be between 2 and 30")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while number > 0:
        result = digits[number % base] + result
        number //= base

    return result


def get_dec_hex_palindrome(x):
    """
    Finds the largest number less than x that is a palindrome in
    hexadecimal and decimal.

    :param x: Upper limit
    :return: The largest hexadecimal and decimal palindrome less than x

    >>> get_dec_hex_palindrome(1000)
    585
    >>> get_dec_hex_palindrome(600)
    585
    >>> get_dec_hex_palindrome(500)
    494
    """
    for num in range(x - 1, 0, -1):
        dec_palindrome = is_palindrome(str(num))
        hex_palindrome = is_palindrome(to_base(num, 16).upper())
        if dec_palindrome and hex_palindrome:
            return num
