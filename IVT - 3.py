# """
# STRUKTURA

"""
a = 5;
b = 6;

if a > b:
    print("číslo", a,"je větší než", b)
elif a < b:
    print("číslo"
          , a,
          "je " \
          "menší " \
          "než"
          , b)
else:
    print("číslo", a,"je stejný jako", b)

a   =   5
b  =       6

c=   a+b
print(c)
"""

# časté CHYBY
# IndentationalError - špatné nebo chybějící odsazení
"""
a = 1
b = 3
if a > b:
print(f"{a} se rovná {b}")
else:
print(a, "se nerovná", b)
"""
# SyntaxError - špatný zápis
"""
print("ahoj"
"""
# NameError - použití nevytvořené proměnné
"""
c = a + b
"""
# TypeError - číslo + text
"""
c = 10 + "jablko"
"""
# ValueError - jiný datový typ
"""
int(input("Zadejte celé čislo: "))
"""
# ZeroDivisionError - dělení nulou
"""
c = 10 / 0
"""
# IndexError - pokus o přístup k neexistujícímu prvku v seznamu
"""
seznam = ["jablko","banán"]
print(seznam[3])
"""
# KeyError - pokus o přístupu k neexistujícímu klíči ve slovníku
"""
slovnik = {"pondělí": 1, "úterý": 3, "středa": 60}
print(slovnik["neděle"])
"""
# AttributeError - pokus o získání neexistujícího attributu z objektu
"""
class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed  = speed

warrior = Character(100, 50, 10)
ninja = Character(80, 40, 40)

print(f"Warrior defense: {warrior.defense}")
print(f"Ninja health: {ninja.health}")
"""


# PROMĚNNÉ a DATOVÉ TYPY
"""
a = (2)                         # int - celé číslo
b = (3.14)                      # float - reálné číslo
c = ("Ahoj")                    # str - řetězec
d = (True)                      # bool - true/flase
e = ["jablko","banán"]          # list - seznam
f = ("jablko","banán")          # tuple - neměnný seznam
g = {"jablko": 10,"banán": 20}  # dict - slovník
h = {"jablko","banán"}          # set - množina bez duplicit
i = range(5)                    # range - rozsah hodnot v cyklech
"""