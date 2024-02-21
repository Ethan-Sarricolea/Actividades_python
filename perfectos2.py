"""
Escribe un programa que imprima todos los números perfectos hasta N
"""

"""
En la funcion factores(n)
Obtenemos los factores del numero (n)
"""

def factores(n):
  numeros = []
  for i in range(1,n+1):
    if n%i==0:
        if i==n:            # Quitamos el factor si es el mismo numero
            continue
        else:
           numeros.append(i)
  return numeros            # Obtenemos la lista de factores


"""
En la funcion perfectos hacemos la suma de los factores
y comparamos con el numero, si son iguales el numero es perfecto
"""

def perfectos(n,numeros):       #recibe el numero y lista de factores actual
    suma=0
    for i in numeros:
        suma+=i

    if (suma==n):
      return True
    else:
      return False

number = int(input("Ingresa el numero maximo: "))

for n in range(1,number+1):
    numerosList = factores(n)       #Lista de factores del numero actual
    print(f"{n} es un numero perfecto" if perfectos(n,numerosList) else
        f"{n} no es un numero perfecto")
