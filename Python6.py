x = int(input("Kolik chcete zadat známek?\n "))
seznam_znamek = []

for i in range(x):
    while True:
        try:
            a = int(input("Zapište známku: "))
            if 0 < a <= 5:
                seznam_znamek.append(a)
                break
            else: 
                print("Známka není na škále od 1 do 5.")
        except:
            print("Známka není na škále od 1 do 5.")


print(f"\nVaše zadané známky jsou: {seznam_znamek}")

def vypocet_prumeru(seznam_znamek):
    soucet = sum(seznam_znamek)
    vysledek = soucet / x
    print(f"Pruměr vašich známek je: {vysledek}")
    return(vysledek)

prumer = vypocet_prumeru(seznam_znamek)

if prumer >= 3:
    print("Je co zlepšovat\n")
else:
    print("Skvělá práce\n")