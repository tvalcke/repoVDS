from math import gcd


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE :
            * none
        POST :
            *un objet Fraction simplifié au maximum est créé
        RAISE :
            * TypeError si les arguments ne sont pas deux entiers
            * ValueError si le dénominateur est nul
        """
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError(
                'Les arguments doivent tous les deux êtres des entiers'
            )
        if den == 0:
            raise ValueError("Le dénominateur ne pas peut etre nul")

        # Simplifier la fraction

        common_divisor = gcd(num, den)
        num //= common_divisor
        den //= common_divisor

        # Je veux faire en sorte d'avoir le den positif
        if den < 0:
            num = -num
            den = -den

        self.__num = num
        self.__den = den

    @property
    def numerator(self):
        """Retourne le numérateur de la fraction"""
        return self.__num

    @property
    def denominator(self):
        """Retourne le dénominateur de la fraction"""
        return self.__den

# ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE :
            * aucun
        POST :
            * retourne la représentation textuelle de
            la fraction réduite au maximum
        """
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the
        fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE :
            *aucun
        POST :
            * si le num > den, le résultat va inclure la partie entière
            et une fraction propre
            * si le num < den, le résultat correspond à une fraction
            équivalente (numérateur / dénominateur) sous forme réduite
        """
        if self.denominator == 1:
            return str(self.numerator)
        if abs(self.numerator) > abs(self.denominator):
            entier = self.numerator // self.denominator
            reste = abs(self.numerator % self.denominator)

            if reste != 0:
                return f"{entier} {reste}/{abs(self.denominator)}"
            else:
                return f"{entier}"

        elif abs(self.numerator) < abs(self.denominator):
            return str(self)

# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE :
            * none
         POST :
            * la sortie est une nouvelle fraction qui est équivalente à la
            somme de self et other
        RAISE :
            * TypeError si other n'est pas une fraction
         """
        if not isinstance(other, Fraction):
            raise TypeError("les deux parametres doivent etre une fraction")
        num = (
            self.numerator * other.denominator +
            other.numerator * self.denominator
        )
        den = self.denominator * other.denominator

        return Fraction(num, den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

         PRE :
            * none
         POST :
            * retourne une nouvelle fraction qui est équivalente à la
            différence
        RAISE :
            * TypeError si other n'est pas une fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("les deux parametres doivent etre une fraction")
        # j'ajoute la fraction négative de other pour calculer la nouvelle
        return self + Fraction(-other.numerator, other.denominator)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE :
            * none
        POST :
            * retourne la multiplication des deux fractions, toujours sous
            forme de fraction
        RAISE :
            * TypeError si other n'est pas une fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("les deux parametres doivent etre une fraction")
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator

        return Fraction(num, den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE :
            * none
        POST :
            * retourne une nouvelle fraction qui est le quotient des paramètres
         RAISE :
            * TypeError si other n'est pas une fraction
            * ZeroDivisionError si le dénominateur est 0
        """
        if not isinstance(other, Fraction):
            raise TypeError("les deux parametres doivent etre une fraction")
        if other.numerator == 0:
            raise ZeroDivisionError("on ne poet pas diviser par 0")

        return self * Fraction(other.denominator, other.numerator)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE :
            * none
        POST :
            * élève le num et le den à une puissance et retourne cette
            nouvelle fraction
        RAISE :
            * TypeError si other other n'est pas un entier
        """
        if not isinstance(other, int):
            raise TypeError("other doit etre un entier")

        return Fraction(self.numerator ** other, self.denominator ** other)

    def __eq__(self, other):
        """Overloading of the == operator for fractions
        PRE :
            * none
        POST :
            * retourne true si les fractions sont équivalentes, sinon
            renvoie false
        RAISE :
            * TypeError si other n'est pas une fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError(
                "La comparaison est définie uniquement entredeux fractions."
            )
        return (self.numerator * other.denominator ==
                self.denominator * other.numerator
                )

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE :
            *aucun
        POST :
            * retourne la fraction en float
        """
        return self.numerator / self.denominator

# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE :
            * aucun
        POST :
            * retourne True si la fraction est égale à 0, return False sinon
        """
        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : aucun
        POST :
            * Retourne True si la fraction est un entier, False sinon
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : RIENNNN
        POST : return true si la fraction est propre, false sinon
        """
        return abs(self.numerator) < abs(self.denominator)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : aucun
        POST :
            * Retourne True si la fraction est une unité, False sinon
        """
        plusGrndDiviseurCmn = gcd(self.numerator, self.denominator)
        return abs(self.numerator // plusGrndDiviseurCmn) == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference
        them is a unit fraction

        PRE :
            * none
        POST :
            * Retourne True si la différence est de la forme ±1/d, False sinon
            (si c'est une fraction unitaire)
        RAISE :
            * TypeError si other n'est pas une fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("other doit etre une fraction")

        diff = self - other
        isAdjacent = abs(diff.numerator) == 1
        isDenValid = abs(diff.denominator) > 0

        return isAdjacent and isDenValid
