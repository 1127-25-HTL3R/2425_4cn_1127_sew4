
__author__ = "Felix Friesenbichler"
__email__ = "1127@htl.rennweg.at"
__license__ = "GPLv2"

import re
from typing import List
from collections import Counter


class Caesar:
    def __init__(self, key: str) -> None:
        """
        Initialisiert den Caesar-Chiffre mit einem Schlüssel (key).

        :param key: Der Verschiebewert für die Chiffrierung.
        """
        self.key = key

    def to_lowercase_letter_only(self, plaintext: str) -> str:
        """
        Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen,
        die keine Kleinbuchstaben aus dem Bereich [a..z] sind.

        :param plaintext: Der Eingabetext.
        :return: Bereinigter Text nur mit Kleinbuchstaben von a-z.

        >>> caesar = Caesar()
        >>> caesar.to_lowercase_letter_only("Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine Kleinbuchstaben aus dem Bereich [a..z] sind.")
        'wandeltdenplaintextinkleinbuchstabenumundentferntallezeichendiekeinekleinbuchstabenausdembereichazsind'
        """
        return "".join(re.findall(r'[a-z]', plaintext.lower()))

    def encrypt(plaintext: str, key: str = None) -> str:
        """
        Key ist ein Buchstabe, der definiert, um wieviele Zeichen verschoben
        wird. Falls kein key übergeben wird, nimmt encrypt den Wert von
        Property.

        Verschlüsselt einen Text nach Caesar-Chiffre mit dem key.

        :param plaintext: Der Eingabetext.
        :param key: Der Verschiebewert für die Chiffrierung.

        :return: Verschlüsselter Text.

        >>> caesar=Caesar("b")
        >>> caesar.key
        'b'
        >>> caesar.encrypt("hallo")
        'ibmmp'
        >>> caesar.encrypt("hallo", "c")
        'jcnnq'
        >>> caesar.encrypt("xyz", "c"
        'zab'
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        shift = alphabet.index(
            key.lower()) if key else alphabet.index(self.key)
        return "".join(alphabet[(alphabet.index(char) + shift) % 26] for char in plaintext)

    def decrypt(crypttext: str, key: str = None) -> str:
        """
        Entschlüsselt einen Text nach Caesar-Chiffre mit dem key.

        :param crypttext: Der verschlüsselte Text.
        :param key: Der Verschiebewert für die Chiffrierung.

        :return: Entschlüsselter Text.

        >>> caesar=Caesar("b")
        >>> caesar.key
        'b'
        >>> caesar.decrypt("ibmmp")
        'hallo'
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        shift = alphabet.index(
            key.lower()) if key else alphabet.index(self.key)
        return "".join(alphabet[(alphabet.index(char) - shift) % 26] for char in crypttext)

    def crack(crypttext: str, elements: int = 1) -> List[str]:
        """
        Berechnet eine Liste mit den wahrscheinlichsten Schlüsseln. Die Länge
        der Liste wird mit elements vorgegeben.

        :param crypttext: Der verschlüsselte Text.
        :param elements: Die gewünschte Länge der Ausgabeliste.

        :return: Eine Liste mit den wahrscheinlichsten Schlüsseln.

        >>>str='Vor einem großen Walde wohnte ein armer Holzhacker mit seiner Frau und seinen
zwei Kindern; das Bübchen hieß Hänsel und das Mädchen Gretel. Er hatte wenig zu beißen
und zu brechen, und einmal, als große Teuerung ins Land kam, konnte er das tägliche Brot
nicht mehr schaffen. Wie er sich nun abends im Bette Gedanken machte und sich vor Sorgen
herumwälzte, seufzte er und sprach zu seiner Frau: "Was soll aus uns werden? Wie können
wir unsere armen Kinder ernähren da wir für uns selbst nichts mehr haben?"'
        >>> caesar = Caesar()
        >>> caesar.crack(str)
        ['a']
        >>> caesar.crack(str, 100) # mehr als 26 können es nicht sein.
        ['a', 'j', 'n', 'o', 'e', 'w', 'd', 'q', 'z', 'p', 'i', 'h', 'y', 's', 'k', 'x', 'c',
'v', 'g', 'b', 'r', 'l']
        >>> crypted = caesar.encrypt(str, "y")
        >>> caesar.crack(crypted, 3)
        ['y', 'h', 'l']
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        frequency_order = "enistardulcgmobwfkzvphjyxq"

        letter_counts = Counter(crypttext)
        most_common_letter = letter_counts.most_common(1)[0][0]

        probable_keys = []
        for frequent_letter in frequency_order:
            shift = (alphabet.index(most_common_letter) -
                     alphabet.index(frequent_letter)) % 26
            probable_keys.append(alphabet[shift])

        return probable_keys[:min(elements, 26)]


class Vigenere:

    def __init__(self, key: str) -> None:
        """
        Initialisiert den Caesar-Chiffre mit einem Schlüssel (key).

        :param key: Der Verschiebewert für die Chiffrierung.
        """
        self.key = key

    def to_lower_case_letter_only(plaintext: str) -> str:
        """
        Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen,
        die keine Kleinbuchstaben aus dem Bereich [a..z] sind.

        :param plaintext: Der Eingabetext.
        :return: Bereinigter Text nur mit Kleinbuchstaben von a-z.

        >>> vigenere = Vigenere()
        >>> Vigenere.to_lowercase_letter_only("Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine Kleinbuchstaben aus dem Bereich [a..z] sind.")
        'wandeltdenplaintextinkleinbuchstabenumundentferntallezeichendiekeinekleinbuchstabenausdembereichazsind'
        """
        return Caesar.to_lowercase_letter_only(plaintext)

    def encrypt(plaintext: str, key: str = None) -> str:
        """
        Verschlüsselt den eingegebnen Text mit dem Vigenere-Verfahren.
        Wenn kein Schlüssel angegeben wird, wird der Property Schlüssel verwedenet.
        """
        plaintext = Vigenere.to_lower_case_letter_only(plaintext)
        key = key if key else Vigenere.key

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        ciphertext = []
        key_index = 0

        for char in plaintext
            # Find the index of the current character in alphabet
            char_index = alphabet.index(char)
            key_char_index = alphabet.index(key[key_index % len(key)])

            # Encrypt the character by shifting it based on the key
            encrypted_char = alphabet[(char_index + key_char_index) % 26]
            ciphertext.append(encrypted_char)
            key_index += 1

        return "".join(cipertext)
