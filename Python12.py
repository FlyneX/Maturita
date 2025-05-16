x = int(input("Zadejte celé číslo:"))

prvocisla = []

for i in range(2, x + 1):
    je_prvocislo = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            je_prvocislo = False
            break
    if je_prvocislo:
        prvocisla.append(i)

print(prvocisla)
