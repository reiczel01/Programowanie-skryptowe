haslo = input("podaj haslo")
for wykrzyknik in haslo:
    if wykrzyknik == "!":
        kk = "1"
        break
if len(haslo) >= 11 and kk == "1":
    print("haslo jest poprawne")
else:
    print("haslo jest nie poprawne")

items = [1, 5, 3, 2, 2, 4, 2, 4]
items = set(items)
print(items)

import math
silnia = input("podaj silnie")
print(math.factorial(int(silnia)))


