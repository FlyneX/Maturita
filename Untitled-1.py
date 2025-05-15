def jednoduchy_faktorial(n):
  """Jednoduchý výpočet faktoriálu pro kladná celá čísla a nulu."""
  if n == 0:
    return 1  # 0! = 1
  
  vysledek = 1
  for i in range(1, n + 1): # Smyčka od 1 do n
    vysledek = vysledek * i # Násobíme
  return vysledek