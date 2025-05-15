ovoce = ["jablo","melon","okurec"]

"""
# Vymění na pozici 1 (v seznamu 2. pozice) proměnnou
ovoce[1] = "paprika"
print(ovoce)

# Přidá na konec
ovoce.append("brambora")
print(ovoce)

# Vloží na pozici 1 (v seznamu 2. pozice)
ovoce.insert(1, "melon")
print(ovoce)

# Odendá proměnnou
ovoce.remove("paprika")
print(ovoce)

# Odendá pozici
ovoce.pop(3)
print(ovoce)
"""
print("")
ovoce.append("melon")
ovoce.append("melon")

ovoce.insert(4, "kedlubna")

print(ovoce)

print(len(ovoce))
print(sorted(ovoce))
print(ovoce.count("melon"))
print(ovoce.index("melon"))

for i in ovoce:
    print(i)