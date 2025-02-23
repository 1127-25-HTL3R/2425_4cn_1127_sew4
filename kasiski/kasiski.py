
__author__ = "Felix Friesenbichler"
__email__ = "1127@htl.rennweg.at"
__license__ = "GPLv2"

import re
from typing import List, Set, Tuple
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
        Berechnet die Abstände zwischen allen Vorkommnissen des Teilstrings im
        verschlüsselten Text.

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

    def dist_n_tuple(self, text: str, laenge: int) -> Set[Tuple[str, int]]:
        """
        Überprüft alle Teilstrings aus text mit der gegebenen laenge und
        liefert ein Set mit den Abständen aller Wiederholunghen der Teilstrings
        in text.

        :param text: Der zu analysierende Text.
        :param laenge: Die Länge der Teilstrings, deren Abstände berechnet werden sollen.

        :return: Ein Tupel der Abstände zwischen den Teilstrings.

        >>> k = Kasiski()
        >>> k.dist_n_tuple("heissajuchei", 2) == {('ei', 9), ('he', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 3) == {('hei', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 4) == set()
        True
        >>> k.dist_n_tuple("heissajucheieinei", 2) == \
            {('ei', 5), ('ei', 14), ('ei', 3), ('ei', 9), ('ei', 11), ('he', 9), ('ei', 2)}
        True
        """
        substring_positions = {}

        # Durchlaufe den Text und extrahiere alle Teilstrings der angegebenen Länge
        for i in range(len(text) - laenge + 1):
            substring = text[i:i + laenge]

            # Füge die Position des Teilstrings zur Liste der Positionen hinzu
            if substring not in substring_positions:
                substring_positions[substring] = []
            substring_positions[substring].append(i)

        # Berechne die Abstände zwischen allen Vorkommnissen von Teilstrings, die mehr als einmal vorkommen
        distances = set()

        for substring, positions in substring_positions.items():
            if len(positions) > 1:
                # Berechne die Abstände zwischen allen Positionen für den aktuellen Teilstring
                for i in range(len(positions)):
                    for j in range(i + 1, len(positions)):
                        distances.add((substring, positions[j] - positions[i]))

        return distances

    def dist_n_list(self, text: str, laenge: int) -> List[int]:
        """
        Wie dist_n_tuple, liefert aber nur eine aufsteigend sortierte Liste der
        Abstände ohne den Text zurück. In der Liste soll kein Element mehrfach
        vorkommen.

        :param text: Der zu analysierende Text.
        :param laenge: Die Länge der Teilstrings, deren Abstände berechnet werden sollen.

        :return: Eine aufsteigend sortierte Liste der Abstände zwischen den Teilstrings.

        >>> k = Kasiski()
        >>> k.dist_n_list("heissajucheieinei", 2)
        [2, 3, 5, 9, 11, 14]
        >>> k.dist_n_list("heissahucheieinei", 3)
        [9]
        >>> k.dist_n_list("heissajucheieinei", 4)
        []
        """
        substring_positions = {}

        # Durchlaufe den Text und extrahiere alle Teilstrings der angegebenen Länge
        for i in range(len(text) - laenge + 1):
            substring = text[i:i + laenge]

            # Füge die Position des Teilstrings zur Liste der Positionen hinzu
            if substring not in substring_positions:
                substring_positions[substring] = []
            substring_positions[substring].append(i)

        # Berechne die Abstände und füge sie zu einer Menge hinzu (damit keine Duplikate entstehen)
        distances = set()

        for positions in substring_positions.values():
            if len(positions) > 1:
                # Berechne die Abstände zwischen allen Positionen
                for i in range(len(positions)):
                    for j in range(i + 1, len(positions)):
                        distances.add(positions[j] - positions[i])

        # Sortiere die Abstände und gebe sie als Liste zurück
        return sorted(distances)

    def ggt(self, x: int, y: int) -> int:
        """
        Ermittelt den größten gemeinsamen Teiler von x und y.

        :param x: Die erste Zahl.
        :param y: Die zweite Zahl.

        :return: Der größte gemeinsame Teiler von x und y.

        >>> k = Kasiski()
        >>> k.ggt(10, 25)
        5
        >>> k.ggt(18, 24)
        6
        """
        while y != 0:
            x, y = y, x % y
        return x

    def ggt_count(self, zahlen: List[int]) -> Counter:
        """
        Bestimmt die Häufigkeit der paarsweisen ggt aller Zahlen aus list.

        :param zahlen: Eine Liste von ganzen Zahlen.
        :return: Ein Counter-Objekt, das die Häufigkeit der berechneten GGT-Werte speichert.

        >>> k = Kasiski()
        >>> k.ggt_count([12, 14, 16]) == Counter({2: 2, 12: 1, 4: 1, 14: 1, 16: 1})
        True
        >>> k.ggt_count([10, 25, 50, 100]) == Counter({10: 3, 25: 3, 50: 2, 5: 1, 100: 1})
        True
        """
        ggt_counter = Counter()

        for zahl in zahlen:
            ggt_counter[zahl] += 1

        for i in range(len(zahlen)):
            for j in range(i + 1, len(zahlen)):
                ggt_wert = self.ggt(zahlen[i], zahlen[j])
                ggt_counter[ggt_wert] += 1

        return ggt_counter

    def get_nth_letter(self, s: str, start: int, n: int) -> str:
        """
        Extrahiert aus s jeden n-ten Buchstaben beginnend mit index start.

        :param s: Der Eingabestring, aus dem Buchstaben extrahiert werden sollen.
        :param start: Der Startindex für die Extraktion.
        :param n: Das Intervall für die Extraktion

        :return: Ein String mit den extrahierten Buchstaben.

        >>> k = Kasiski()
        >>> k.get_nth_letter("Das ist kein kreativer Test.", 1, 4)
        'asektrs'
        """

        return s[start::n]

    def crack_key(self, length: int) -> str:
        """
        Bestimmt den wahrscheinlichsten Schlüssel mit gegebener Länge.

        :param length: Die vermutete Länge des Schlüssels
        :return: The most likely key.
        """

        substrings = ['' for _ in range(length)]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i, char in enumerate(self.crypttext):
            substrings[i % length] += char

        key = []
        for substring in substrings:
            letter_counts = Counter(substring)
            most_common_letter = letter_counts.most_common(1)[0][0]

            shift = alphabet.index(most_common_letter) - alphabet.index('e')

            shift = shift % 26

            key.append(alphabet[shift])

        return ''.join(key)



if __name__ == "__main__":

    message = """Ihr naht euch wieder, schwankende Gestalten,
Die früh sich einst dem trüben Blick gezeigt.
Versuch ich wohl, euch diesmal festzuhalten?
Fühl ich mein Herz noch jenem Wahn geneigt?
Ihr drängt euch zu! nun gut, so mögt ihr walten,
Wie ihr aus Dunst und Nebel um mich steigt;
Mein Busen fühlt sich jugendlich erschüttert
Vom Zauberhauch, der euren Zug umwittert.

Ihr bringt mit euch die Bilder froher Tage,
Und manche liebe Schatten steigen auf;
Gleich einer alten, halbverklungnen Sage
Kommt erste Lieb und Freundschaft mit herauf;
Der Schmerz wird neu, es wiederholt die Klage
Des Lebens labyrinthisch irren Lauf,
Und nennt die Guten, die, um schöne Stunden
Vom Glück getäuscht, vor mir hinweggeschwunden.

Sie hören nicht die folgenden Gesänge,
Die Seelen, denen ich die ersten sang;
Zerstoben ist das freundliche Gedränge,
Verklungen, ach! der erste Widerklang.
Mein Lied ertönt der unbekannten Menge,
Ihr Beifall selbst macht meinem Herzen bang,
Und was sich sonst an meinem Lied erfreuet,
Wenn es noch lebt, irrt in der Welt zerstreuet.

Und mich ergreift ein längst entwöhntes Sehnen
Nach jenem stillen, ernsten Geisterreich,
Es schwebet nun in unbestimmten Tönen
Mein lispelnd Lied, der Äolsharfe gleich,
Ein Schauer faßt mich, Träne folgt den Tränen,
Das strenge Herz, es fühlt sich mild und weich;
Was ich besitze, seh ich wie im Weiten,
Und was verschwand, wird mir zu Wirklichkeiten."""

    key = "abcd"
    vigenere = Vigenere(key)
    encrypted_message = vigenere.encrypt(message)
    print("Verschlüsselter Text:", encrypted_message)

    kasiski = Kasiski(encrypted_message)

    probable_lengths = kasiski.dist_n_list(encrypted_message, 3)
    print("Wahrscheinliche Schlüssel-Längen", probable_lengths)

    if probable_lengths:
        probable_key_length = probable_lengths[0]
        print(f"Vermutete Schlüssel-Länge: {probable_key_length}")

        cracked_key = kasiski.crack_key(probable_key_length)
        print(f"Vermuteter Schlüssel: {cracked_key}")

        decrypted_message = vigenere.decrypt(encrypted_message, cracked_key)
        print("Entschlüsselter Text: ", decrypted_message)

    else:
        print("Konnte keine Schlüssel-Länge bestimmen.")
