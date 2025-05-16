sporty = ["atletika", "hokej", "golf", "cyklistika", "bobování", "šachy", "plavání", "motosport", "fotbal", "vzpírání"]

#print(len(sporty))
#print(sorted(sporty))
#sporty.reverse()
#print(sporty)

zadany_sport = input("Zadej sport:")
if zadany_sport in sporty:
    print(sporty.index(zadany_sport))
if zadany_sport not in sporty:     
    print("sport není v seznamu")

#print(sporty.count("fotbal"))

#sporty.remove("hokej")
#sporty.append("parkour")
#for sport in sporty:
#    print(sport)

