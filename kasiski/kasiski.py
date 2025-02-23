
__author__ = "Felix Friesenbichler"
__email__ = "1127@htl.rennweg.at"
__license__ = "GPLv2"

import re


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
        shift = alphabet.index(key.lower()) if key else alphabet.index(self.key)
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
