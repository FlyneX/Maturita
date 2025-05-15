# Definuje porměnné mimo cyklus
j = 2

# Zjistí, do jakého čísla chceme vypsat prvočísla
# Také zajistí, že zadáné číslo je číslo a je větší než 1 (čísla < 2 nejsou prvočísla)
while True:
    cislo = input("Zadej přirozené číslo větší než 1:\n ")
    try:
        cislo = int(cislo)
        if cislo < 2:
            print("Číslo není větší než 1")
            continue    # Continue přeskočí zbytek cyklu a vrátí se na začátek cyklu
        break           # Ukončí cyklus
    except:             # V případě erroru se provede tato část (hodnota není datový typ int)
        print("Hodnota není číslo.")


# Funkce na zjištění, zda číslo je prvočíslo
def je_prvocislo(num):
    for i in range(2, int(num**0.5)+1): # Pokud má složené číslo(čísla co nejsou prvočísla) dělitele většího než jeho odmocnina, musí mít i dělitele menšího než jeho odmocnina
        if num%i==0:
            return None
    return num


# Vypíše prvočísla do zadaného čísla
print("Prvočísla jsou:")
while j <= int(cislo):
    prime=je_prvocislo(j)
    if prime is not None:
        print(prime, end=' ')
    j+=1