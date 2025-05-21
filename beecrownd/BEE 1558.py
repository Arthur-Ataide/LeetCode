import math
try:
  while True:
    n = int(input())
    if n < 0:
      print("NO")
      continue
    menor = 0
    maior = int(math.sqrt(n))
    
    menor_acao = True
    
    while maior >= 0 or maior >= menor:
      if maior ** 2 + menor ** 2 == n:
        print("YES")
        break
      
      if menor_acao and maior ** 2 + menor ** 2 < n:
        menor += 1
      
      if maior ** 2 + menor ** 2 > n:
        maior -= 1
    
    if maior ** 2 + menor ** 2 != n:
      print("NO")
except EOFError:
  pass