
__author__ = "Felix Friesenbichler"
__email__ = "1127@htl.rennweg.at"
__license__ = "GPLv2"

import re
from typing import List, Set
from collections import Counter


class Caesar:
    def __init__(self, key: str="e") -> None:
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

    def encrypt(self, plaintext: str, key: str = None) -> str:
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
        >>> caesar.encrypt("xyz", "c")
        'zab'
        """
        plaintext = self.to_lowercase_letter_only(plaintext)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        shift = alphabet.index(
            key.lower()) if key else alphabet.index(self.key)
        return "".join(alphabet[(alphabet.index(char) + shift) % 26] for char in plaintext)

    def decrypt(self, crypttext: str, key: str = None) -> str:
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

    def crack(self, crypttext: str, elements: int = 1) -> List[str]:
        """
        Berechnet eine Liste mit den wahrscheinlichsten Schlüsseln. Die Länge
        der Liste wird mit elements vorgegeben.

        :param crypttext: Der verschlüsselte Text.
        :param elements: Die gewünschte Länge der Ausgabeliste.

        :return: Eine Liste mit den wahrscheinlichsten Schlüsseln.

        >>> message='Vor einem großen Walde wohnte ein armer Holzhacker mit seiner Frau und seinen zwei Kindern; das Bübchen hieß Hänsel und das Mädchen Gretel. Er hatte wenig zu beißen und zu brechen, und einmal, als große Teuerung ins Land kam, konnte er das tägliche Brot nicht mehr schaffen. Wie er sich nun abends im Bette Gedanken machte und sich vor Sorgen herumwälzte, seufzte er und sprach zu seiner Frau: "Was soll aus uns werden? Wie können wir unsere armen Kinder ernähren da wir für uns selbst nichts mehr haben?"'
        >>> caesar = Caesar()
        >>> caesar.crack(message)
        ['a']
        >>> caesar.crack(message, 100) # mehr als 26 können es nicht sein.
        ['a', 'r', 'w', 'm', 'l', 'e', 'n', 'b', 'k', 't', 'c', 'y', 's', 'q', 'd', 'i', 'z', 'u', 'f', 'j', 'p', 'x', 'v', 'g', 'h', 'o']
        >>> crypted=caesar.encrypt(message, "y")
        >>> caesar.crack(crypted, 3)
        ['y', 'p', 'u']
        """
        crypttext = self.to_lowercase_letter_only(crypttext)
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

    def __init__(self, key: str = "a") -> None:
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

        >>> vigenere = Vigenere()
        >>> vigenere.to_lowercase_letter_only("Wandelt den plaintext in Kleinbuchstaben um und entfernt alle Zeichen, die keine Kleinbuchstaben aus dem Bereich [a..z] sind.")
        'wandeltdenplaintextinkleinbuchstabenumundentferntallezeichendiekeinekleinbuchstabenausdembereichazsind'
        """
        c = Caesar()
        return c.to_lowercase_letter_only(plaintext)

    def encrypt(self, plaintext: str, key: str = None) -> str:
        """
        Verschlüsselt den eingegebnen Text mit dem Vigenere-Verfahren.
        Wenn kein Schlüssel angegeben wird, wird der Property Schlüssel verwedenet.

        :param plaintext: Der Klartext, der verschlüsselt werden soll.
        :param key: Der Schlüssel, der für die Verschlüsselung verwendet wird.

        :return: Der verschlüsselte Text.

        >>> vigenere = Vigenere(key="abc")
        >>> vigenere.encrypt("hello world")
        'hfnlpyosnd'

        >>> vigenere.encrypt("world hello", key="cba")
        'yprnehgmlq'
        """
        plaintext = self.to_lowercase_letter_only(plaintext)
        key = key if key else self.key

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        ciphertext = []
        key_index = 0

        for char in plaintext:
            # Find the index of the current character in alphabet
            char_index = alphabet.index(char)
            key_char_index = alphabet.index(key[key_index % len(key)])

            # Encrypt the character by shifting it based on the key
            encrypted_char = alphabet[(char_index + key_char_index) % 26]
            ciphertext.append(encrypted_char)
            key_index += 1

        return "".join(ciphertext)

    def decrypt(self, ciphertext: str, key: str = None) -> str:
        """
        Entschlüsselt den eingegebenen Text mit dem Vigenere-Verfahren.
        Wenn kein Schlüssel angegebnm wird, wird der Property Schlüssel verwendet.

        :param ciphertext: Der verschlüsselte Text, der entschlüsselt werden soll.
        :param key: Der Schlüssel, der verwendet werden soll.

        :return: Der entschlüsselte Text.

        >>> vigenere = Vigenere(key="abc")
        >>> vigenere.decrypt("hfnlpyosnd")
        'helloworld'

        >>> vigenere.decrypt("yprnehgmlq", key="cba")
        'worldhello'
        """

        v = Vigenere()
        ciphertext = v.to_lowercase_letter_only(ciphertext)
        key = key if key else self.key

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        plaintext = []
        key_index = 0

        for char in ciphertext:
            # Find the index of the current character in the alphabet
            char_index = alphabet.index(char)
            key_char_index = alphabet.index(key[key_index % len(key)])

            # Decrypt the character by shifting it based on the key
            decrypted_char = alphabet[(char_index - key_char_index) % 26]
            plaintext.append(decrypted_char)
            key_index += 1

        return "".join(plaintext)

class Kasiski:

    def __init__(self, crypttext: str = "") -> None:
        """
        Initalisiert die Klasse mit dem gegebenen Text

        :param crypttext: Der verschlüsselte Text.
        """
        self.crypttext = crypttext


    def allpos(self, text: str, teilstring: str) -> List[int]:
        """
        Berechnet die Positionen von teilstring in text.

        :param text: Der Text, in dem nach dem Teilstring gesucht wird.
        :param teilstring: Der Teilstring, nach dem gesucht wird.
        :return: Eine Liste der Startpositionen, an denen der Teilstring im Text gefunden wurde.

        >>> k = Kasiski()
        >>> k.allpos("heissajuchei, ein ei", "ei")
        [1, 10, 14, 18]

        >>> k.allpos("heissajuchei, ein ei", "hai")
        []
        """
        positions = []
        start = 0

        while True:
            # Suchen des Teilstrings ab der aktuellen Position
            start = text.find(teilstring, start)

            if start == -1:
                break

            positions.append(start)
            start += 1

        return positions

    def alldist(self, text: str, teilstring: str) -> Set[int]:
        """
        Berechnet die Abstände zwischen allen Vorkommnissen des Teilstrings im verschlüsselten Text.

        :param text: Der Text, in welchem die Abstände gesucht werden sollen.
        :param teilstring: Der Teilstring, wo die Abstände zwischeneinander gezählt werden sollen.
        :return: Ein Set mit den Abständen.

        >>> k = Kasiski()
        >>> k.alldist("heissajuchei, ein ei", "ei")
        {4, 8, 9, 13, 17}
        >>> k.alldist("heissajuchei, ein ei", "hai")
        set()
        """
        positions = []

        index = text.find(teilstring)
        while index != -1:
            positions.append(index)
            index = text.find(teilstring, index + 1)

        distances = set()
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                distances.add(positions[j] - positions[i])

        return distances
