"""
Escribe un programa en python que genere el triangulo de Pascal hasta n filas
"""

def triangulo(i,j):
  if j==0 or j==i:
    return 1
  else:
    return triangulo(i-1,j-1)+triangulo(i-1,j)

def print_triangulo(n):
  for i in range(n):
    for i in range(i+1):
      print(triangulo(i,j),end=" ")
    print()

print_triangulo(int(input("Numero de filas: ")))
