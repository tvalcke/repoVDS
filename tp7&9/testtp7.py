from tp7 import Fraction

# Création des fractions pour les tests
fraction1 = Fraction(3, 4)
fraction2 = Fraction(5, 4)
fraction3 = Fraction(7, 4)
fraction4 = Fraction(3, 4)  # Identique à fraction1 pour tester l'égalité

# Test de la somme
fraction_sum = fraction1 + fraction2
# Attendu: (3/4) + (5/4) = 8/4 (ou 2)
print(f"fraction1 + fraction2 = {fraction_sum.numerator}/"
      f"{fraction_sum.denominator}")


# Test de l'égalité
print(f"fraction1 == fraction2: {fraction1 == fraction2}")  # Attendu: False
print(f"fraction1 == fraction4: {fraction1 == fraction4}")  # Attendu: True

# Test de conversion en float
fraction1_as_float = float(fraction1)
print(f"fraction1 en float: {fraction1_as_float}")  # Attendu: 0.75

# Test d'adjacence
print(
    f"fraction1 est adjacente à fraction2: {
        fraction1.is_adjacent_to(fraction2)
    }"
)  # Attendu: True, car |(5/4) - (3/4)| = 1/4

print(
    f"fraction1 est adjacente à fraction3: {
        fraction1.is_adjacent_to(fraction3)
    }"
)  # Attendu: False, car différence n'est pas ±1/d

# Test avec den nul
try:
    fraction_invalid = Fraction(1, 0)
except ValueError as e:
    # Attendu : "Le dénominateur ne peut pas être nul"
    print(f"Erreur de création de fraction: {e}")
