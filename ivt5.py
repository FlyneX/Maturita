def funkce(a,b):
    try:
        c = a - b
        if c > 0:
            print(f"{c} je kladne cislo")
        elif c < 0:
            print(f"{c} je zaporne cislo")
        else:
            print(f"{c} je nula")
    except NameError:
        print("promenna a nebo b neni definovana")


