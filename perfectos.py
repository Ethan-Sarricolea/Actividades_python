"""
Escribe un programa en python que diga si un número es perfecto
"""

numeros = []

"""
En la funcion factores(n)
Obtenemos los factores del numero (n)
"""

def factores(n):
  for i in range(1,n+1):
    if n%i==0:
        if i==n:            # Quitamos el factor si es el mismo numero
            continue
        else:
           numeros.append(i)
  return numeros


"""
En la funcion perfectos hacemos la suma de los factores
y comparamos con el numero, si son iguales el numero es perfecto
"""

def perfectos(n):
    suma=0
    for i in numeros:
        suma+=i

    if (suma==n):
      return True
    else:
      return False

n = int(input("Ingresa un numero: "))
factores(n)
print(f"{n} es un numero perfecto" if perfectos(n) else
       f"{n} no es un numero perfecto")
