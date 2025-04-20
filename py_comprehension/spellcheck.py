__author__ = "Felix Friesenbichler"
__email__ = "1127@htl.rennweg.at"
__license__ = "GPLv2"

from typing import Set, List, Tuple


def read_all_words(filename: str) -> Set[str]:
    """
    Liest alle Wörter einer Datei ein und gibt diese dann in einem Set zurück.

    :param filename: Die Datei, die eingelesen werden soll.
    :return: Das Set, welches alle Wörter der Datei enthält.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return {line.strip().lower() for line in f if line.strip()}


def split_word(wort: str) -> List[Tuple[str, str]]:
    """
    Bestimmt eine Liste aller Aufteilungen des Wortes. Die Listenelemente
    bestehen aus Tupel mit den Elementen head und tail.

    :param wort: Das Wort, welches aufgeteilt werden soll.
    :return: Eine Liste, welche Tupel enthält, bestehend aus head und tail

    >>> split_word("abc")
    [ ("", "abc"), ("a", "bc"), ("ab", "c"), ("abc", "") ]
    """
    return [(wort[:i], wort[i:]) for i in range(len(wort) + 1)]


def edit1(wort: str) -> Set[str]:
    """
    Findet alle Wörter mit Edit-Distanz eins (= ein Tippfehler).
    Es liefert ALLE Möglichkeiten zurück.

    :param wort: Das Wort, welches auf Tippfehler geprüft werden soll.
    :return: Die Möglichkeiten, wie das Wort korrigiert werden könnte.
    """

    letters = 'abcdefghijklmnopqrstuvwxyzäöüß'
    splits = split_word(wort)
    deletes = {L + R[1:] for L, R in splits if R}
    transposes = {L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1}
    replaces = {L + c + R[1:] for L, R in splits if R for c in letters}
    inserts = {L + c + R for L, R in splits for c in letters}
    return set(deletes | transposes | replaces | inserts)



def edit1_good(wort: str, alle_woerter: List[str]) -> Set[str]:
    """
    Ruft edit1(wort) auf und liefert nur die richtigen Wörter, welche auch im
    Wörterbuch vorhanden sind.

    :param wort: Das Wort, für welches Verbesserungsvorschläge angezeigt werden
    sollen.
    :param alle_woerter: Ein Set von Wörtern für die gecheckt werden soll.
    :return: Die Möglichkeiten, wie das Wort korrigiert werden könnte.
    """

    return {w for w in edit1(wort) if w in alle_woerter}



def edit2_good(wort: str, alle_woerter: List[str]) -> Set[str]:
    """
    Bestimmt Wörter mit Edit-Distanz zwei.

    :param wort: Das Wort, für welches Verbesserungsvorschläge angezeigt werden
    sollen.
    :param alle_woerter: Ein Set von Wörtern für die gecheckt werden soll.
    :return: Die Möglichkeiten, wie das Wort korrigiert werden könnte.
    """

    print("Placeholder")


def correct(word: str, alle_woerter: List[str]) -> Set[str]:
    """
    Findet die Korrekturen für word als "Liste"

    :param wort: Das Wort, für welches Verbesserungsvorschläge angezeigt werden
    sollen.
    :param alle_woerter: Ein Set von Wörtern für die gecheckt werden soll.
    :return: Die Möglichkeiten, wie das Wort korrigiert werden könnte.
    """

    print("Placeholder")


if __name__ == "__main__":

    woerter = read_all_words("de-en.txt")
    assert (sorted(correct("Aalsuppe", woerter)) == ['aalquappe', 'aalsuppe',
                                                     'aalsuppen'])
    assert (sorted(correct("Alsuppe", woerter)) == ['aalsuppe', 'aalsuppen',
                                                    'suppe', 'ursuppe'])
    assert (sorted(correct("Alsupe", woerter)) == ['aalsuppe', 'absude',
                                                   'alse', 'lupe'])

    print("Evertyhing worked!")
