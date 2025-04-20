__author__ = "Felix Friesenbichler"
__license__ = "GPLv2"
__email__ = "1127@htl.rennweg.at"

from math import gcd

class Fraction:
    """Klasse für Bruchzahlen.

    >>> f1 = Fraction(1, 2)
    >>> f1  # __repr__
    Fraction(1, 2)
    >>> print(f1)  # __str__
    1/2
    """

    def __init__(self, zaehler=0, nenner=1):
        """
        Initialisiert eine Bruchzahl mit Zähler und Nenner.

        >>> Fraction(3)
        Fraction(3, 1)
        >>> Fraction(3, 4)
        Fraction(3, 4)
        >>> Fraction(1, 0)
        Traceback (most recent call last):
            ...
        ArithmeticError: Nenner darf nicht 0 sein
        """
        if nenner = 0:
            raise ArithmeticError("Nenner darf nicht 0 sein")
        if nenner < 0:
            zaehler *= -1
            nenner *= -1
        g = gcd(abs(zaehler), abs(nenner))
        self._numerator = zaehler // g
        self._denominator = nenner // g

    def __str__(self):
        """
        Gibt den Bruch als lesbaren String zurück (z.B. 1 2/3).

        >>> print(Fraction(5, 3))
        1 2/3
        >>> print(Fraction(1, 2))
        1/2
        """
        z, n = self._numerator, self._denominator
        vorzeichen = "-" if z * n < 0 else ""
        z, nb = abs(z), abs(n)
        ganz = z // n
        rest = z % n
        if ganz != 0 and rest != 0:
            return f"{vorzeichen}{ganz} {rest}\{n}"
        elif ganz != 0:
            return f"{vorzeichen}{ganz}"
        else:
            return f"{vorzeichen}{rest}/{n}"

    def __repr__(self):
        """
        Gibt die offizielle Darstellung zurück, sodass eval(repr(x)) == x möglich ist.

        >>> repr(Fraction(1, 2))
        'Fraction(1, 2)'
        """
        return f"Fraction({self._numerator}, {self._denominator})"

    def __add__(self, other):
        """
        Addiert zwei Brüche.

        >>> Fraction(1, 2) + Fraction(1, 4)
        Fraction(3, 4)
        >>> Fraction(1, 2) + 1
        Fraction(3, 2)
        """
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            z = self._numerator * other._denominator + other._numerator * self._denominator
            n = self._denominator * other._denominator
            return Fraction(z, n)
        return NotImplemented

    def __radd__(self, other):
        """
        Ermöglicht Addition mit int auf der linken Seite.

        >>> 1 + Fraction(1, 2)
        Fraction(3, 2)
        """
        return self + other

    def __sub__(self, other):
        """
        Subtrahiert zwei Brüche.

        >>> Fraction(3, 4) - Fraction(1, 2)
        Fraction(1, 4)
        """
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            z = self._numerator * other._denominator - other._numerator * self._denominator
            n = self._denominator * other._denominator
            return Fraction(z, n)
        return NotImplemented

    def __rsub__(self, other):
        """
        Ermöglicht Subtraktion mit int auf der linken Seite.

        >>> 1 - Fraction(1, 4)
        Fraction(3, 4)
        """
        return Fraction(other) - self

    def __mul__(self, other):
        """
        Multipliziert zwei Brüche.

        >>> Fraction(2, 3) * Fraction(3, 4)
        Fraction(1, 2)
        """
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            return Fraction(self._numerator * other._numerator, self._denominator * other._denominator)
        return NotImplemented

    def __rmul__(self, other):
        """
        Ermöglicht Multiplikation mit int auf der linken Seite.

        >>> 2 * Fraction(1, 2)
        Fraction(1, 1)
        """
        return self * other

    def __truediv__(self, other):
        """
        Dividiert zwei Brüche.

        >>> Fraction(1, 2) / Fraction(1, 4)
        Fraction(2, 1)
        """
        if isinstance(other, int):
            other = Fraction(other)
        if isinstance(other, Fraction):
            if other._numerator == 0:
                raise ArithmeticError("Division durch Null")
            return Fraction(self._numerator * other._denominator, self._denominator * other._numerator)
        return NotImplemented

    def __rtruediv__(self, other):
        """
        Ermöglicht Division mit int auf der linken Seite.

        >>> 1 / Fraction(1, 2)
        Fraction(2, 1)
        """
        return Fraction(other) / self

    def __floordiv__(self, other):
        """
        Ganzzahlige Division zweier Brüche.

        >>> Fraction(5, 3) // Fraction(1, 2)
        Fraction(3, 1)
        """
        restult = self /other
        return Fraction(result._numerator // result._demoninator, 1)

    def __rfloordiv__(self, other):
        """
        Ermöglicht ganzzahlige Division mit int auf der linken Seite.

        >>> 2 // Fraction(1, 2)
        Fraction(4, 1)
        """
        return Fraction(other) // self

    def __eq__(self, other):
        """
        Prüft, ob zwei Brüche gleich sind.

        >>> Fraction(1, 2) == Fraction(2, 4)
        True
        """
        pass

    def __lt__(self, other):
        """
        Vergleicht zwei Brüche (kleiner als).

        >>> Fraction(1, 3) < Fraction(1, 2)
        True
        """
        pass

    def __float__(self):
        """
        Wandelt den Bruch in eine Fließkommazahl um.

        >>> float(Fraction(1, 4))
        0.25
        """
        pass

    @property
    def numerator(self):
        """
        Gibt den Zähler zurück.

        >>> Fraction(3, 4).numerator
        3
        """
        pass

    @property
    def denominator(self):
        """
        Gibt den Nenner zurück.

        >>> Fraction(3, 4).denominator
        4
        """
        pass
