# Definuje proměnné mimo cyklus
faktor = 1
vysledek = 1

# Zjistí, z jakého čísla chceme udělat faktorial
# Zajistí, že zadané číslo je nezáporné a že se opravdu jedná o číslo
while True:
    faktorial = input("Zadej nezáporné číslo:\n")
    try:                # Pokud zde nastane Error, ukončí se zbytek try a spustí se except
        faktor = int(faktorial)
        if faktor <0:
            print("Zadané číslo je záporné.")
            continue    # Continue přeskočí zbytek cyklu a vrátí se na začátek cyklu
        break           # Ukončí cyklus
    except:             # V případě erroru se provede tato část (hodnota není datový typ int)
        print("Zadáná hodnota není číslo.")


# vypočet faktorialu
for i in range(faktor, 0, -1):
    vysledek *= i


# vypíše náš faktorial
print(f"{faktor}! = {vysledek}")